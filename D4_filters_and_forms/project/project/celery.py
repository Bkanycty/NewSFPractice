import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Реализовать еженедельную рассылку с последними новостями (каждый понедельник в 8:00 утра).
app.conf.beat_schedule = {
    'weekly_spam': {
        'task': 'news.tasks.weekly_spammer',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': None,
    },
}

app.autodiscover_tasks()


