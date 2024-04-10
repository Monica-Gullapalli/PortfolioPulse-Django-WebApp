from django.apps import AppConfig
from django.core.mail import send_mail

class FinAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fin_app"
