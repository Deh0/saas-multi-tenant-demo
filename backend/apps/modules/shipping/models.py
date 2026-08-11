from django.db import models
from django.utils.translation import gettext_lazy as _

class Shipping(models.Model):
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="shippings",
        verbose_name=_("Pedido")
    )
    shipping_method = models.CharField(_("Método de Envio"), max_length=50)
    tracking_number = models.CharField(_("Número de Rastreamento"), max_length=100, blank=True, null=True)
    price = models.DecimalField(_("Preço do Frete"), max_digits=10, decimal_places=2)
    delivery_date = models.DateField(_("Data de Entrega"), blank=True, null=True)
    delivery_status = models.CharField(_("Status da Entrega"), max_length=20, default="pending")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
    
    def __str__(self):
        return f"Envio #{self.id} - {self.shipping_method} - {self.delivery_status}"
