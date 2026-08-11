from django.db import models
from django.utils.translation import gettext_lazy as _

class Invoice(models.Model):
    order = models.ForeignKey(
        "orders.Order", 
        on_delete=models.CASCADE,
        related_name="invoices",
        verbose_name=_("Pedido")
    )
    invoice_number = models.CharField(_("Número da Fatura"), max_length=100)
    amount = models.DecimalField(_("Valor"), max_digits=10, decimal_places=2)
    issued_date = models.DateField(_("Data de Emissão"))
    due_date = models.DateField(_("Data de Vencimento"))
    status = models.CharField(_("Status"), max_length=20, default="pending")

    access_key = models.CharField(_("Chave de Acesso"), max_length=255, blank=True, null=True)
    danfe_url = models.URLField(_("URL da DANFE"), blank=True, null=True)
    xml_url = models.URLField(_("URL do XML"), blank=True, null=True)
    sefaz_protocol = models.CharField(_("Protocolo SEFAZ"), max_length=255, blank=True, null=True)
    rejection_reason = models.TextField(_("Motivo de Rejeição"), blank=True, null=True)

    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"Fatura #{self.invoice_number} - {self.amount} - {self.status}"

class DigitalCertificate(models.Model):
    tenant = models.OneToOneField(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='digital_certificate',
        verbose_name=_('Tenant')
    )
    certificate_name = models.CharField(_("Nome do Certificado"), max_length=255)
    certificate_file = models.FileField(_("Arquivo do Certificado"), upload_to='certificates/')
    certificate_password = models.CharField(_("Senha do Certificado"), max_length=255)
    expiration_date = models.DateField(_("Data de Expiração"))

    STATUS_CHOICES = [
        ('active', _("Ativo")),
        ('expired', _("Expirado")),
        ('revoked', _("Revogado")),
        ('inactive', _("Inativo")),
    ]
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.certificate_name
    
class FiscalInformation(models.Model):
    tenant = models.OneToOneField(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='fiscal_information',
        verbose_name=_('Tenant')
    )
    cnpj = models.CharField(_("CNPJ"), max_length=18)
    state_registration = models.CharField(_("Inscrição Estadual"), max_length=20)
    municipal_registration = models.CharField(_("Inscrição Municipal"), max_length=20)

    TAX_REGIME_CHOICES = [
        ('simples_nacional', _("Simples Nacional")),
        ('lucro_presumido', _("Lucro Presumido")),
        ('lucro_real', _("Lucro Real")),
        ('microempreendedor_individual', _("Microempreendedor Individual (MEI)")),
    ]
    tax_regime = models.CharField(_("Regime Tributário"), max_length=50, choices=TAX_REGIME_CHOICES, default='simples_nacional')
    cnae = models.CharField(_("CNAE"), max_length=20)
    legal_name = models.CharField(_("Razão Social"), max_length=255)
    trade_name = models.CharField(_("Nome Fantasia"), max_length=255)
    status = models.BooleanField(_("Status"), default=True)

    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.cnpj