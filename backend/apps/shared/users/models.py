from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    cpf = models.CharField(_("CPF"), max_length=14, unique=True)
    name = models.CharField(_("Nome"), max_length=255)
    surname = models.CharField(_("Sobrenome"), max_length=255)
    email = models.EmailField(_("Email"), unique=True)
    phone_number = models.CharField(_("Número de Telefone"), max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(_("Data de Nascimento"), blank=True, null=True)
    password = models.CharField(_("Senha"), max_length=255)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.email
    
class Address(models.Model): 
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("Usuário")
    )
    cep = models.CharField(_("CEP"), max_length=9)
    street = models.CharField(_("Logradouro"), max_length=255)
    number = models.CharField(_("Número"), max_length=20)
    complement = models.CharField(_("Complemento"), max_length=255, blank=True, null=True)
    city = models.CharField(_("Cidade"), max_length=30)
    state = models.CharField(_("Estado"), max_length=2)
    district = models.CharField(_("Bairro"), max_length=255)

    ADDRESS_TYPE = [
        ("residential", "Residencial"),
        ("commercial", "Comercial"),
        ("delivery", "Entrega"),
        ("billing", "Cobrança"),
    ]
    address_type = models.CharField(
        _("Tipo de Endereço"),
        max_length=20, 
        choices=ADDRESS_TYPE,
        default="residential"
    )
    status = models.CharField(_("Status"), max_length=20, default="active")
    is_main = models.BooleanField(_("Endereço Principal"), default=False)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}/{self.state}"
    
class Role(models.Model):
    tenant = models.ForeignKey(
        "tenants.Tenant", 
        on_delete=models.CASCADE,
        related_name="roles",
        verbose_name=_("Empresa")
    )
    name = models.CharField(_("Nome"), max_length=255)
    description = models.TextField(_("Descrição"), blank=True, null=True)
    permissions = models.JSONField(_("Permissões"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name="employee_profile",
        verbose_name=_("Usuário")
    )
    tenant = models.ForeignKey(
        "tenants.Tenant", 
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name=_("Empresa")
    )
    role = models.ForeignKey(
        Role, 
        on_delete=models.SET_NULL,
        related_name="employees",
        verbose_name=_("Cargo"),
        blank=True,
        null=True
    )
    corporate_email = models.ForeignKey(
        "tenants.CorporateEmail", 
        on_delete=models.SET_NULL,
        related_name="employees",
        verbose_name=_("Email Corporativo"),
        blank=True,
        null=True
    )
    employee_function = models.CharField(_("Função"), max_length=255, blank=True, null=True)
    salary = models.DecimalField(_("Salário"), max_digits=10, decimal_places=2, blank=True, null=True)
    schedule = models.CharField(_("Horário de Trabalho"), max_length=255, blank=True, null=True)
    admission_date = models.DateField(_("Data de Admissão"), blank=True, null=True)
    termination_date = models.DateField(_("Data de Demissão"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, default="active")
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"{self.user.name} {self.user.surname} - {self.role.name if self.role else 'Sem Cargo'}"
    
class UserMaster(models.Model):
    MASTER_TYPE_CHOICES = [
        ("primary", "Master Principal"),
        ("financial", "Master Financeiro"),
        ("operational", "Master Operacional"),
        ("administrative", "Master Administrativo"),
    ]
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name="master_profile",
        verbose_name=_("Usuário")
    )
    tenant = models.ForeignKey(
        "tenants.Tenant", 
        on_delete=models.CASCADE,
        related_name="masters",
        verbose_name=_("Empresa")
    )
    master_type = models.CharField(
        _("Tipo de Master"),
        max_length=20, 
        choices=MASTER_TYPE_CHOICES,
        default="primary"
    )
    can_manage_billing = models.BooleanField(_("Pode Gerenciar Cobrança"), default=False)
    can_manage_users = models.BooleanField(_("Pode Gerenciar Usuários"), default=False)
    can_manage_domains = models.BooleanField(_("Pode Gerenciar Domínios"), default=False)
    can_manage_contracts = models.BooleanField(_("Pode Gerenciar Contratos"), default=False)

    status = models.CharField(_("Status"), max_length=20, default="active")
    is_primary = models.BooleanField(_("Usuário Primário"), default=False)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    def __str__(self):
        return f"{self.user.name} {self.user.surname} - {self.get_master_type_display()}"
    
class LGPDConsent(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='lgpd_consents',
        verbose_name=_('Usuário')
    )
    CONSENT_TYPE = [
        ('marketing', _('Marketing')),
        ('privacy_policy', _('Política de Privacidade')),
        ('terms_of_use', _('Termos de Uso')),
        ('cookies', _('Cookies')),
        ('data_processing', _('Processamento de Dados')),
    ]
    consent_type = models.CharField(_('Tipo de Consentimento'), max_length=50, choices=CONSENT_TYPE, default='marketing')
    accepted = models.BooleanField(_('Aceito'), default=False)
    ip_address = models.GenericIPAddressField(_('Endereço IP'), null=True, blank=True)
    accepted_at = models.DateTimeField(_('Aceito em'), null=True, blank=True)
    expires_at = models.DateTimeField(_('Expira em'), null=True, blank=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Consentimento LGPD')
        verbose_name_plural = _('Consentimentos LGPD')
    def __str__(self):
        return f'{self.user.email} - {self.consent_type} - {"Aceito" if self.accepted else "Não Aceito"}'