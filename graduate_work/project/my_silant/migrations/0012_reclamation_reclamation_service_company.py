# Generated by Django 4.1.5 on 2023-02-11 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_silant', '0011_alter_reclamation_recovery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamation',
            name='reclamation_service_company',
            field=models.ForeignKey(blank=True, default=1, help_text='выберите из списка', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reclamation_service_company', to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания'),
        ),
    ]