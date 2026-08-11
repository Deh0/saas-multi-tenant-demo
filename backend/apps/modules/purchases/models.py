from django.db import models
from django.utils.translation import gettext_lazy as _

class PurchaseRequest(models.Model):
    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='purchase_requests',
        verbose_name=_('Tenant')
    )
    supplier = models.ForeignKey(
        'suppliers.Supplier',
        on_delete=models.CASCADE,
        related_name='purchase_requests',
        verbose_name=_('Supplier')
    )
    requested_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='purchase_requests',
        verbose_name=_('Requested By')
    )
    status = models.CharField(_('Status'), max_length=20, default='pending')
    request_at = models.DateTimeField(_('Request At'), auto_now_add=True)
    expected_delivery_at = models.DateTimeField(_('Expected Delivery At'), null=True, blank=True)
    notes = models.TextField(_('Notes'), blank=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Purchase Request')
        verbose_name_plural = _('Purchase Requests')
    def __str__(self):
        return f'{self.supplier} - {self.requested_by} - {self.status}'
    
class PurchaseRequestItem(models.Model):
    purchase_request = models.ForeignKey(
        PurchaseRequest,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_('Purchase Request')
    )
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='purchase_request_items',
        verbose_name=_('Product')
    )
    product_variant = models.ForeignKey(
        'catalog.ProductVariant',
        on_delete=models.CASCADE,
        related_name='purchase_request_items',
        verbose_name=_('Product Variant')
    )
    quantity = models.DecimalField(_('Quantity'), max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField(_('Unit Cost'), max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(_('Subtotal'), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Purchase Request Item')
        verbose_name_plural = _('Purchase Request Items')
    def __str__(self):
        return f'{self.product} - {self.quantity} x {self.unit_cost}'

        