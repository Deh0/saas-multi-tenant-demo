from django.apps import AppConfig


class ShippingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.modules.shipping"
    label = "shipping"
    verbose_name = "Shipping"
