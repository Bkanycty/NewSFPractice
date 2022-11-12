from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    cooking = models.TextField(verbose_name='Приготовление', default='Похоже, здесь пока нет рецепта')

    def __str__(self):
        return f"id: {self.pk} name: {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    categoryRecipe = models.ManyToManyField(Recipe, through='CategoryRecipe')

    def __str__(self):
        return f"id: {self.pk} name: {self.name}"


class CategoryRecipe(models.Model):
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipeThrough = models.ForeignKey(Recipe, on_delete=models.CASCADE)
