from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

class Campaign(models.Model):
    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='campaigns',
        verbose_name=_('Tenant')
    )
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True)

    CAMPAIGN_TYPE_CHOICES = [
        ('email', _('Email')),
        ('sms', _('SMS')),
        ('instagram', _('Instagram')),
        ('facebook', _('Facebook')),
        ('google_ads', _('Google Ads')),
        ('manual', _('Manual')),
    ]
    campaign_type = models.CharField(_('Campaign Type'), max_length=50, choices=CAMPAIGN_TYPE_CHOICES, default='manual')
    start_date = models.DateField(_('Start Date'))
    end_date = models.DateField(_('End Date'))
    budget = models.DecimalField(_('Budget'), max_digits=10, decimal_places=2)
    status = models.CharField(_('Status'), max_length=20)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Campaign')
        verbose_name_plural = _('Campaigns')
    def __str__(self):
        return self.name
    
