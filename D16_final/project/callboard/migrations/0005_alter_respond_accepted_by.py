# Generated by Django 4.0.5 on 2022-06-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0004_alter_respond_accepted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respond',
            name='accepted_by',
            field=models.TextField(null=True, verbose_name='Принят пользователем'),
        ),
    ]
