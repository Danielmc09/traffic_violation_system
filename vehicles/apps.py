from django.apps import AppConfig
from django.db.models.signals import post_migrate


class VehiclesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicles'

    def ready(self):
        from .signals import load_fixtures
        post_migrate.connect(load_fixtures, sender=self)