# Generated by Django 4.1.3 on 2022-11-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking',
            field=models.TextField(default='Похоже, здесь пока нет рецепта', verbose_name='Приготовление'),
        ),
    ]
