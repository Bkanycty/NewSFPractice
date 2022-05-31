from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory


# напишем уже знакомую нам функцию обнуления товара на складе
def nullify_rating(modeladmin, request,
                    queryset):  # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(rating=0)


nullify_rating.short_description = 'Обнулить рейтинг статьи'  # описание для более понятного представления в админ панеле задаётся, как будто это объект


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('id', 'author', 'title', 'has_rating')
    list_filter = ('id', 'author', 'title')
    search_fields = ('author', 'title')
    actions = [nullify_rating]


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)
