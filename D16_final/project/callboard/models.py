from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ckeditor.fields import RichTextField

class Author(models.Model):
    authorUser = models.OneToOneField(User, help_text='Автор', verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.authorUser)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, help_text='Название категории', verbose_name='Категория')

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    author = models.ForeignKey(Author, verbose_name='Автор', help_text='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = RichTextField()
    postResponds = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'


class Respond(models.Model):
    author = models.ForeignKey(Author, verbose_name='Автор', help_text='Автор', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Объявление', help_text='Объявление', on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    text = models.TextField(verbose_name='Текст')
    accepted_by = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return str(self.pk) + ': ' + str(self.author) + ' ' + str(self.post) + ': ' + str(self.text) + ': ' + str(
            self.accepted_by)

    def accept(self, user):
        self.accepted_by = user
        self.save()
