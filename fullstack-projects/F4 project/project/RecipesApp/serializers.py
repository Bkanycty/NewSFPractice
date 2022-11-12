from .models import *
from rest_framework import serializers


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'categoryRecipe', ]


class RecipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'cooking', ]
