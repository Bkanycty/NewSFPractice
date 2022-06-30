# Generated by Django 4.0.2 on 2022-06-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_category_name_en_us_category_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_en_us',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en_us',
            field=models.CharField(max_length=128, null=True, verbose_name='Оглавление'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Оглавление'),
        ),
    ]
