from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView  # импортируем класс получения деталей объекта
from .models import Post, Category, Author, PostCategory
from .filters import NewsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.core.cache import cache
from django.utils.translation import gettext as _  # импортируем функцию для перевода

from django.utils import timezone

import pytz  # импортируем стандартный модуль для работы с часовыми поясами


# Create your views here.

class Index(View):
    def get(self, request):
        string = _('Привет мир')

        return HttpResponse(string)


class CategoriesList(ListView):
    # model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'
    queryset = Category.objects.order_by('name')

    def get(self, request):
        # . Translators: This message appears on the home page only
        models = Category.objects.all()

        context = {
            'models': models,
        }

        return HttpResponse(render(request, 'categories.html', context))


class NewsList(ListView):
    # model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10

    def get(self, request):
        current_time = timezone.localtime()

        # .  Translators: This message appears on the home page only
        posts = Post.objects.all()

        context = {
            'posts': posts,
            'current_time': current_time,
            'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
        }

        return HttpResponse(render(request, 'posts.html', context))

    #  по пост-запросу будем добавлять в сессию часовой пояс, который и будет обрабатываться написанным нами ранее middleware
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/news/')


# дженерик для получения деталей о товаре
class NewsDetail(DetailView):
    template_name = 'post.html'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}',
                        None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj


class NewsSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')

    def get_context_data(self,
                         **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['news_filter'] = NewsFilter(self.request.GET,
                                            queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = NewsForm
    permission_required = ('news.add_post',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

    def post(self, request, *args, **kwargs):

        title = request.POST['title']
        text = request.POST['text']
        post_category_id = request.POST['postCategory']
        category_object = Category.objects.get(id=post_category_id)
        if Author.objects.filter(authorUser__username=request.user.username).exists():
            author = Author.objects.get(authorUser__username=request.user.username).id
        else:
            author = Author.objects.create(authorUser=request.user).id
        new_post = Post.objects.create(author_id=author, title=title, text=text)

        new_postcategory = PostCategory.objects.create(postThrough=new_post, categoryThrough=category_object)

        new_postcategory.save()
        new_post.save()

        return redirect('news_list')


# дженерик для редактирования объекта
class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    form_class = NewsForm
    permission_required = ('news.change_post',)

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


# дженерик для удаления товара
class NewsDelete(LoginRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/news/')


class Celebrities(ListView):
    model = Post
    template_name = 'celebrities.html'
    context_object_name = 'celebrities'
    queryset = Post.objects.filter(postCategory__name='Знаменитости').order_by('-dateCreation')


@login_required
def subscribe_celebrities(request):
    user = request.user
    Category.objects.get(name='Знаменитости').subscribers.add(user)

    return redirect('/news/Знаменитости/')


class Games(ListView):
    model = Post
    template_name = 'games.html'
    context_object_name = 'games'
    queryset = Post.objects.filter(postCategory__name='Игры').order_by('-dateCreation')


@login_required
def subscribe_games(request):
    user = request.user
    Category.objects.get(name='Игры').subscribers.add(user)

    return redirect('/news/Игры/')


class Cooking(ListView):
    model = Post
    template_name = 'cooking.html'
    context_object_name = 'cooking'
    queryset = Post.objects.filter(postCategory__name='Кулинария').order_by('-dateCreation')


@login_required
def subscribe_cooking(request):
    user = request.user
    Category.objects.get(name='Кулинария').subscribers.add(user)

    return redirect('/news/Кулинария/')


class News(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'cat_news'
    queryset = Post.objects.filter(postCategory__name='Новости').order_by('-dateCreation')


@login_required
def subscribe_news(request):
    user = request.user
    Category.objects.get(name='Новости').subscribers.add(user)

    return redirect('/news/Новости/')


class Politics(ListView):
    model = Post
    template_name = 'politics.html'
    context_object_name = 'politics'
    queryset = Post.objects.filter(postCategory__name='Политика').order_by('-dateCreation')


@login_required
def subscribe_politics(request):
    user = request.user
    Category.objects.get(name='Политика').subscribers.add(user)

    return redirect('/news/Политика/')


class Sport(ListView):
    model = Post
    template_name = 'sport.html'
    context_object_name = 'sport'
    queryset = Post.objects.filter(postCategory__name='Спорт').order_by('-dateCreation')


@login_required
def subscribe_sport(request):
    user = request.user
    Category.objects.get(name='Спорт').subscribers.add(user)

    return redirect('/news/Спорт/')


class Technologies(ListView):
    model = Post
    template_name = 'technologies.html'
    context_object_name = 'technologies'
    queryset = Post.objects.filter(postCategory__name='Технологии').order_by('-dateCreation')


@login_required
def subscribe_technologies(request):
    user = request.user
    Category.objects.get(name='Технологии').subscribers.add(user)

    return redirect('/news/Технологии/')


class Humor(ListView):
    model = Post
    template_name = 'humor.html'
    context_object_name = 'humor'
    queryset = Post.objects.filter(postCategory__name='Юмор').order_by('-dateCreation')


@login_required
def subscribe_humor(request):
    user = request.user
    Category.objects.get(name='Юмор').subscribers.add(user)

    return redirect('/news/Юмор/')
