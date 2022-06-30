from django.apps import AppConfig


class CallboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'callboard'


    def ready(self):
        from callboard import signals

