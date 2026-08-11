from django.db import models
from django.utils.translation import gettext_lazy as _

class Coupon(models.Model):
    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='coupons',
        verbose_name=_('Tenant')
    )
    code = models.CharField(_('Code'), max_length=50, unique=True)
    description = models.TextField(_('Descrição'), blank=True)

    DISCOUNT_TYPES = [ 
        ('percentage', _('Porcentagem')),
        ('fixed', _('Valor Fixo')),
        ('free_shipping', _('Frete Grátis')),
    ]
    discount_type = models.CharField(_('Tipo de Desconto'), max_length=20, choices=DISCOUNT_TYPES, default='percentage')
    discount_value = models.DecimalField(_('Valor do Desconto'), max_digits=10, decimal_places=2)
    minium_purchase_value = models.DecimalField(_('Valor Mínimo de Compra'), max_digits=10, decimal_places=2, null=True, blank=True)
    usage_limit = models.PositiveIntegerField(_('Limite de Uso'), null=True, blank=True)
    usage_count = models.PositiveIntegerField(_('Contagem de Uso'), default=0)
    start_date = models.DateTimeField(_('Data de Início'))
    end_date = models.DateTimeField(_('Data de Término'))
    is_active = models.BooleanField(_('Ativo'), default=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Cupom')
        verbose_name_plural = _('Cupons')
    def __str__(self):
        return self.code
    
class CouponUsage(models.Model):
    coupon = models.ForeignKey(
        Coupon,
        on_delete=models.CASCADE,
        related_name='usages',
        verbose_name=_('Cupom')
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='coupon_usages',
        verbose_name=_('Usuário')
    )
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='coupon_usages',
        verbose_name=_('Pedido')
    )
    discount_value = models.DecimalField(_('Valor do Desconto'), max_digits=10, decimal_places=2)
    used_at = models.DateTimeField(_('Usado em'), auto_now_add=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Uso de Cupom')
        verbose_name_plural = _('Usos de Cupons')
    def __str__(self):
        return f'{self.coupon.code} - {self.user.username} - {self.order.id}'
    