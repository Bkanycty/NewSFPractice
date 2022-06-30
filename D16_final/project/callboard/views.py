from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView
from .models import Author, Category, Post, Respond
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import PostForm, RespondForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .filters import RespondsFilter
from django_filters import FilterSet, ModelChoiceFilter
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'Post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = ('callboard.add_post')

    def post(self, request, *args, **kwargs):

        title = request.POST['title']
        text = request.POST['text']
        req_category = request.POST['category']
        category = Category.objects.get(id=req_category)
        if Author.objects.filter(authorUser__username=request.user.username).exists():
            author = Author.objects.get(authorUser__username=request.user.username).id
        else:
            author = Author.objects.create(authorUser=request.user).id

        new_post = Post.objects.create(author_id=author, category=category, title=title, text=text)
        new_post.save()

        return redirect('posts')


class MyList(ListView):
    model = Respond
    template_name = 'my.html'
    context_object_name = 'responds'
    form_class = PostForm

    def get_queryset(self, **kwargs):
        queryset = Respond.objects.filter(post__author__authorUser__username=self.request.user.username).order_by(
            '-dateCreation')
        return queryset

    paginate_by = 10

    def get_context_data(self,
                         **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['responds_filter'] = RespondsFilter(self.request.GET, queryset=self.get_queryset())
        primary_keys = list(str(*i.values()) for i in
                            Post.objects.filter(author__authorUser__username=self.request.user.username).values('pk'))
        values = list(str(*i.values()) for i in
                      Post.objects.filter(author__authorUser__username=self.request.user.username).values('title'))
        pid_pt = list(zip(primary_keys, values))
        context['choices'] = pid_pt
        context['user'] = self.request.user

        return context


class RespondDetail(DetailView):
    model = Respond
    template_name = 'respond_detail.html'
    context_object_name = 'respond'


class RespondDelete(DeleteView):
    template_name = 'respond_delete.html'
    queryset = Respond.objects.all()
    success_url = '/posts/my/'


def accept_respond(*args, **kwargs):
    respond_id = list(dict(**kwargs).values())[0]
    user_ = User.objects.get(username=list(dict(**kwargs).values())[1])
    Respond.objects.get(pk=respond_id).accepted_by.add(user_)
    Respond.objects.get(pk=respond_id).save()

    post_creator_username = user_.username
    post_creator_post = Respond.objects.get(pk=respond_id).post.text
    receiver_username = Respond.objects.get(pk=respond_id).author.authorUser.username
    receiver_email = Respond.objects.get(pk=respond_id).author.authorUser.email
    receiver_respond_text = Respond.objects.get(pk=respond_id).text
    text = 'Текст'
    html_content = render_to_string(
        'respond_accepted_email.html',
        {
            'post_creator_username': post_creator_username,
            'post_creator_post': post_creator_post,
            'receiver_username': receiver_username,
            'receiver_respond_text': receiver_respond_text,
            'text': text
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'Ваш отклик был принят',
        body=f"{text}",
        from_email='b.kanycty@yandex.ru',
        to=[receiver_email],
    )

    msg.attach_alternative(html_content, "text/html")

    msg.send()

    return redirect('/posts/my/')


class RespondCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'respond_create.html'
    form_class = RespondForm
    permission_required = ('callboard.add_respond',)

    def post(self, request, *args, **kwargs):
        respond_user = self.request.user
        post_author = Author.objects.get(authorUser__username=list(dict(**kwargs).values())[1])
        text = request.POST['text']
        post_ = list(dict(**kwargs).values())[0]

        new_respond = Respond.objects.create(author=post_author, post_id=post_, text=text)
        Post.objects.get(id=post_).postResponds.add(respond_user)
        new_respond.save()
        return redirect('posts')


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = ('post.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


def send_mailing(*args, **kwargs):
    users_to_send = User.objects.all()

    for user in users_to_send:
        if user.is_superuser:
            pass
        elif user.is_staff:
            pass
        else:

            username = user.username
            email = user.email
            title = f'Свежие объявления :)'
            html_content = render_to_string(
                'send_mailing.html',
                {
                    'username': username,
                    'fresh_posts': Post.objects.all()[0:9]
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'{title}',
                body=f"Приветствуем, {username}! Свежие объявления для вас",
                from_email='b.kanycty@yandex.ru',
                to=[email],
            )

            msg.attach_alternative(html_content, "text/html")

            msg.send()

    return redirect('/posts/')
