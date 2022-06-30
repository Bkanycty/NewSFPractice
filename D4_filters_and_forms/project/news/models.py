from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy  # импортируем «ленивый» геттекст с подсказкой


class Author(models.Model):
    # Модель, содержащая объекты всех авторов.
    # Имеет следующие поля:
    # cвязь «один к одному» с встроенной моделью пользователей User;

    authorUser = models.OneToOneField(User, help_text=_('Автор'), verbose_name=_('Автор'), on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    # рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать.
    def update_rating(self):
        # обновляет рейтинг пользователя, переданный в аргумент этого метода.
        # Он состоит из следующего:
        # суммарный рейтинг каждой статьи автора умножается на 3;
        # суммарный рейтинг всех комментариев автора;
        # суммарный рейтинг всех комментариев к статьям автора.

        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.authorUser)


class Category(models.Model):
    # Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
    # Имеет единственное поле: название категории.
    # Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True).
    name = models.CharField(max_length=64, unique=True, help_text=_('Название категории'), verbose_name=_('Категория'))
    subscribers = models.ManyToManyField(User)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class Post(models.Model):
    # Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
    # Каждый объект может иметь одну или несколько категорий.
    # Соответственно, модель должна включать следующие поля:
    # связь «один ко многим» с моделью Author;
    author = models.ForeignKey(Author, verbose_name=_('Автор'), help_text=_('Автор'), on_delete=models.CASCADE)

    # поле с выбором — «статья» или «новость»;
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE, verbose_name=_('Тип'))

    # автоматически добавляемая дата и время создания;
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))

    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
    postCategory = models.ManyToManyField(Category, through='PostCategory', verbose_name=_('Категория'))

    # заголовок статьи/новости;
    title = models.CharField(max_length=128, verbose_name=_('Оглавление'))

    # текст статьи/новости;
    text = models.TextField(verbose_name=_('Текст'))

    # рейтинг статьи/новости.
    rating = models.SmallIntegerField(default=0)

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

    def preview(self):
        return f'{self.text[0:64]} ...'

    def like(self):
        # увеличивают/уменьшают рейтинг на единицу
        self.rating += 1
        self.save()

    def dislike(self):
        # увеличивают/уменьшают рейтинг на единицу
        self.rating -= 1
        self.save()

    def __str__(self):  # __unicode__ on Python 2
        return str(f'Пост (id: {self.pk}, заголовок: {self.title})')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его

    @property
    def has_rating(self):
        if self.rating > 0:
            return 'Положительный'
        elif self.rating < 0:
            return 'Отрицательный'
        else:
            return 'Без рейтинга'


class PostCategory(models.Model):
    #     Промежуточная модель для связи «многие ко многим»:
    # связь «один ко многим» с моделью Post;
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)

    # связь «один ко многим» с моделью Category.
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):  # __unicode__ on Python 2
    #     return str(f'{self.postThrough} <---> Категория ({self.categoryThrough}: {self.categoryThrough.pk})')


class Comment(models.Model):
    # Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
    # Модель будет иметь следующие поля:
    # связь «один ко многим» с моделью Post;
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)

    # связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)

    # текст комментария;
    text = models.TextField()

    # дата и время создания комментария;
    dateCreation = models.DateTimeField(auto_now_add=True)

    # рейтинг комментария.
    rating = models.SmallIntegerField(default=0)

    def like(self):
        # увеличивают/уменьшают рейтинг на единицу
        self.rating += 1
        self.save()

    def dislike(self):
        # увеличивают/уменьшают рейтинг на единицу
        self.rating -= 1
        self.save()
