from django.db import models
from django.utils.translation import gettext_lazy as _
from django_tenants.models import TenantMixin, DomainMixin

class Plan(models.Model):
    name = models.CharField(_("Nome"), max_length=100)
    description = models.TextField(_("Descrição"), blank=True, null=True)
    monthly_price = models.DecimalField(_("Preço Mensal"), max_digits=10, decimal_places=2)
    limit_users = models.PositiveIntegerField(_("Limite de Usuários"), default=5)
    product_limit = models.PositiveIntegerField(_("Limite de Produtos"), default=50)
    monthly_request_limit = models.IntegerField(_("Limite de Requisições Mensais"), default=0)
    is_active = models.BooleanField(_("Ativo"), default=True)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.name
    
class Tenant(TenantMixin):
    auto_create_schema = True # cria automaticamente o schema do tenant ao salvar o modelo
    # Ou seja, todas as empresas serão criadas com seu próprio schema
    # Onde será ligada a um plano, porque não existe Tenant sem plano.

    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="tenants",
        verbose_name=_("Plano")
    )

    cnpj = models.CharField(_("CNPJ"), max_length=18, unique=True, null=True, blank=True)
    cpf = models.CharField(_("CPF"), max_length=14, unique=True, null=True, blank=True)
    corporate_name = models.CharField(_("Razão Social"), max_length=255)
    trade_name = models.CharField(_("Nome Fantasia"), max_length=255, blank=True, null=True)
    email = models.EmailField(_("Email"), unique=True)
    phone_number = models.CharField(_("Número de Telefone"), max_length=20, blank=True, null=True)
    logo_url = models.URLField(_("URL do Logo"), blank=True, null=True)
    description = models.TextField(_("Descrição"), blank=True, null=True)

    STATUS_CHOICES = [
        ("lead", _("Interessado")),
        ("in_touch", _("Em Contato")),
        ("active", _("Ativo")),
        ("inactive", _("Inativo")),
        ("suspended", _("Suspenso")),
    ]

    status = models.CharField(_("Status"), max_length=20, default="active", choices=STATUS_CHOICES)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.corporate_name
    
class DomainTenant(DomainMixin):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="domains",
        verbose_name=_("Empresa"),
    )

    is_main = models.BooleanField(_("Domínio Principal"), default=False)

    STATUS_CHOICES = [
        ("active", _("Ativo")),
        ("inactive", _("Inativo")),
        ("suspended", _("Suspenso")),
    ]

    status = models.CharField(_("Status"), max_length=20, default="active", choices=STATUS_CHOICES)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)


class SubDomainTenant(models.Model):
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE,
        related_name="subdomains",
        verbose_name=_("Empresa")
    )
    domain = models.ForeignKey(
        DomainTenant, 
        on_delete=models.CASCADE,
        related_name="subdomains",
        verbose_name=_("Domínio")
    )
    subdomain = models.CharField(_("Subdomínio"), max_length=255)
    subdomain_type = models.CharField(_("Tipo"), max_length=20, default="subdomain")
    full_url = models.URLField(_("URL Completa"), blank=True, null=True)

    STATUS_CHOICES = [
        ("active", _("Ativo")),
        ("inactive", _("Inativo")),
        ("suspended", _("Suspenso")),
    ]
    status = models.CharField(_("Status"), max_length=20, default="active", choices=Tenant.STATUS_CHOICES)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.subdomain

class CorporateEmail(models.Model):
    # user FK aqui, ainda não criei user
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE,
        related_name="corporate_emails",
        verbose_name=_("Empresa")
    )
    domain = models.ForeignKey(
        DomainTenant, 
        on_delete=models.CASCADE,
        related_name="corporate_emails",
        verbose_name=_("Domínio")
    )
    email = models.EmailField(_("Email Corporativo"), unique=True)

    STATUS_CHOICES = [
        ("active", _("Ativo")),
        ("inactive", _("Inativo")),
        ("suspended", _("Suspenso")),
    ]
    status = models.CharField(_("Status"), max_length=20, default="active", choices=Tenant.STATUS_CHOICES)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.email

