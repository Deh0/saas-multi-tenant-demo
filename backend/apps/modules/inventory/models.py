from django.db import models
from django.utils.translation import gettext_lazy as _

class Stock(models.Model):
    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='stocks',
        verbose_name=_('Tenant')
    )
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='stocks',
        verbose_name=_('Product')
    )
    product_variant = models.ForeignKey(
        'catalog.ProductVariant',
        on_delete=models.CASCADE,
        related_name='stocks',
        verbose_name=_('Product Variant'),
        null=True,
        blank=True
    )
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    minium_quantity = models.IntegerField(verbose_name=_('Minimum Quantity'), default=0)
    reserved_quantity = models.IntegerField(verbose_name=_('Reserved Quantity'), default=0)
    status = models.CharField(max_length=20, verbose_name=_('Status'), default='available')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')
        unique_together = ('tenant', 'product', 'product_variant')
    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"

class StockMovement(models.Model):
    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='stock_movements',
        verbose_name=_('Tenant')
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='movements',
        verbose_name=_('Stock')
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        related_name='stock_movements',
        verbose_name=_('User'),
        null=True,
        blank=True
    )
    MOVIMENT_TYPE_CHOICES = [
        ('entry', _('Entrada')),
        ('exit', _('Saída')),
        ('adjustment', _('Ajuste')),
        ('reservation', _('Reserva')),
        ('release', _('Liberacao')),
    ]
    movement_type = models.CharField(max_length=20, verbose_name=_('Movement Type'), choices=MOVIMENT_TYPE_CHOICES, default='entry')
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    reason = models.CharField(max_length=255, verbose_name=_('Reason'), null=True, blank=True)

    REFERENCE_TYPE_CHOICES = [
        ('order', _('Pedido')),
        ('purchase', _('Compra')),
        ('production', _('Produção')),
        ('manual_adjustment', _('Ajuste Manual')),
        ('return', _('Devolução')),
    ]
    reference_type = models.CharField(max_length=50, verbose_name=_('Reference Type'), choices=REFERENCE_TYPE_CHOICES, null=True, blank=True, default='manual_adjustment')
    reference_id = models.CharField(max_length=50, verbose_name=_('Reference ID'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Stock Movement')
        verbose_name_plural = _('Stock Movements')
