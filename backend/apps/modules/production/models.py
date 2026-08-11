from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductionOrder(models.Model):
    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='production_orders',
        verbose_name=_('Tenant')
    )
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='production_orders',
        verbose_name=_('Product')
    )
    product_variant = models.ForeignKey(
        'catalog.ProductVariant',
        on_delete=models.CASCADE,
        related_name='production_orders',
        verbose_name=_('Product Variant')
    )
    responsible_user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='production_orders',
        verbose_name=_('Responsible User')
    )
    quantity = models.DecimalField(_('Quantidade'), max_digits=10, decimal_places=2)
    status = models.CharField(_('Status'), max_length=50)
    production_type = models.CharField(_('Tipo de Produção'), max_length=50)
    started_at = models.DateTimeField(_('Iniciado em'), null=True, blank=True)
    expected_finished_at = models.DateTimeField(_('Previsão de término'), null=True, blank=True)
    finished_at = models.DateTimeField(_('Finalizado em'), null=True, blank=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Ordem de Produção')
        verbose_name_plural = _('Ordens de Produção')
    def __str__(self):
        return f'{self.product.name} - {self.quantity} unidades'
    
class ProductionStage(models.Model):
    production_order = models.ForeignKey(
        ProductionOrder,
        on_delete=models.CASCADE,
        related_name='stages',
        verbose_name=_('Ordem de Produção')
    )
    responsible_user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='production_stages',
        verbose_name=_('Responsável')
    )
    name = models.CharField(_('Nome do Estágio'), max_length=100)
    stage_order = models.PositiveIntegerField(_('Ordem do Estágio'))
    status = models.CharField(_('Status'), max_length=50)
    expected_finished_at = models.DateTimeField(_('Previsão de término'), null=True, blank=True)
    finished_at = models.DateTimeField(_('Finalizado em'), null=True, blank=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Estágio de Produção')
        verbose_name_plural = _('Estágios de Produção')
        ordering = ['stage_order']
    def __str__(self):
        return f'{self.name} - {self.status}'
    