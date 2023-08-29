"""Apps for PyMySQL."""

from django.apps import AppConfig


class PymysqlConfig(AppConfig):
    """Config for PyMySQL."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "pymysql"
