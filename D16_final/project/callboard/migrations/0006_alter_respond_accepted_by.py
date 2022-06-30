# Generated by Django 4.0.5 on 2022-06-28 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('callboard', '0005_alter_respond_accepted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respond',
            name='accepted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Принят пользователем'),
        ),
    ]
