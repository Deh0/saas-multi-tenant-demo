from django.db import models
from django.utils.translation import gettext_lazy as _

class Supplier(models.Model):
    tenant = models.ForeignKey(
        "tenants.Tenant",
        on_delete=models.CASCADE,
        related_name="suppliers",
        verbose_name=_("Empresa")
    )
    address = models.ForeignKey(
        "users.Address",
        on_delete=models.SET_NULL,
        related_name="suppliers",
        verbose_name=_("Endereço"),
        blank=True,
        null=True
    )
    name = models.CharField(_("Nome"), max_length=255)
    cnpj = models.CharField(_("CNPJ"), max_length=18, unique=True, blank=True, null=True)
    contact_email = models.EmailField(_("Email de Contato"), blank=True, null=True)
    contact_phone = models.CharField(_("Telefone de Contato"), max_length=20, blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
    supplier_type = models.CharField(
        _("Tipo de Fornecedor"), 
        max_length=50,
        default="local"
    )

    def __str__(self):
        return self.name

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="supplier_products",
        verbose_name=_("Fornecedor")
    )
    product = models.ForeignKey(
        "tenants.Tenant",
        on_delete=models.CASCADE,
        related_name="supplier_products",
        verbose_name=_("Produto")
    )
    cost_price = models.DecimalField(_("Preço de Custo"), max_digits=10, decimal_places=2, blank=True, null=True)
    lead_time_days = models.PositiveIntegerField(_("Tempo de Entrega (dias)"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    is_primary = models.BooleanField(_("Fornecedor Principal"), default=False)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"{self.supplier.name} - {self.product.name}"
    
