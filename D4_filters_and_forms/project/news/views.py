# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView  # импортируем класс получения деталей объекта
from .models import Post
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10


# дженерик для получения деталей о товаре
class NewsDetail(DetailView):
    template_name = 'post.html'
    queryset = Post.objects.all()


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
class NewsCreate(CreateView):
    template_name = 'post_create.html'
    form_class = NewsForm


# дженерик для редактирования объекта
class NewsUpdate(UpdateView):
    template_name = 'post_create.html'
    form_class = NewsForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class NewsDelete(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
