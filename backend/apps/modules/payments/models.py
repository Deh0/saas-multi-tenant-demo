from django.db import models
from django.utils.translation import gettext_lazy as _

class Payment(models.Model):
    order = models.ForeignKey(
        "orders.Order", 
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name=_("Pedido")
    )
    payment_method = models.CharField(_("Método de Pagamento"), max_length=50)
    amount = models.DecimalField(_("Valor"), max_digits=10, decimal_places=2)
    status = models.CharField(_("Status"), max_length=20, default="pending")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"Pagamento #{self.id} - {self.payment_method} - {self.amount}"
    
class PaymentAttempt(models.Model):
    payment = models.ForeignKey(
        Payment, 
        on_delete=models.CASCADE,
        related_name="attempts",
        verbose_name=_("Pagamento")
    )
    attempt_number = models.PositiveIntegerField(_("Número da Tentativa"), default=1)
    status = models.CharField(_("Status"), max_length=20, default="pending")
    error_message = models.TextField(_("Mensagem de Erro"), blank=True, null=True)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"Tentativa #{self.attempt_number} - {self.status}"
    