from django.apps import AppConfig


class OnenoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onenote'

    def ready(self) -> None:
        from . import signals