# Generated by Django 4.0.5 on 2022-06-29 16:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('callboard', '0014_remove_respond_accepted_by_respond_accepted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respond',
            name='accepted_by',
        ),
        migrations.AddField(
            model_name='respond',
            name='accepted_by',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
