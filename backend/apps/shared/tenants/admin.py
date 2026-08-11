from django.contrib import admin
from .models import Plan, Tenant, DomainTenant, SubDomainTenant

admin.site.register(Plan)
admin.site.register(Tenant)
admin.site.register(DomainTenant)
admin.site.register(SubDomainTenant)
