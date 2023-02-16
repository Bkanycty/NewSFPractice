# Generated by Django 4.1.5 on 2023-02-11 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_silant', '0014_alter_machine_client_alter_machine_service_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamation',
            name='reclamation_service_company',
        ),
        migrations.AlterField(
            model_name='machine',
            name='client',
            field=models.ForeignKey(blank=True, default='-', help_text='выберите из списка', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='service_company',
            field=models.ForeignKey(blank=True, default='-', help_text='выберите из списка', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_company', to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания'),
        ),
    ]
