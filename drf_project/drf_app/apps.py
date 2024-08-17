"""DRF app config module."""

from django.apps import AppConfig


class DrfAppConfig(AppConfig):
    """DRF app config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drf_app'
