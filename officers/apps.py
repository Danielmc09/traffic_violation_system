from django.apps import AppConfig


class OfficersConfig(AppConfig):
    name = 'officers'

    def ready(self):
        from . import signals
