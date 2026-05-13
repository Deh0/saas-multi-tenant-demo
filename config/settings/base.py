# configuração base utilizada por todos os ambientes, dev e prod
from pathlib import Path
from decouple import config
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR / 'apps'))

# Nunca deve ser commitada no repositório
# deve ser utilizada uma senha para dev e outra para prod
SECRET_KEY = config('SECRET_KEY')

#  Multi-tenant configurações
SHARED_APPS = [ 
    #'django_tenants',


    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # gerencia sites para múltiplos domínios
    'django.contrib.contenttypes',

    # 'apps.shared_public.tenants',
]

TENANT_APPS = [
    'django.contrib.auth',

    # Apps com dados isolados por tenant
    # 'apps.tenant_apps.core',
    # 'apps.tenant_apps.customers',
    # 'apps.tenant_apps.managments',
    # 'apps.tenant_apps.orders',
    # 'apps.tenant_apps.payments',
    # 'apps.tenant_apps.products',
    # 'apps.tenant_apps.reviews',
    # 'apps.tenant_apps.collections',
    # 'apps.tenant_apps.cart',
    # 'apps.tenant_apps.coupons',
    # 'apps.tenant_apps.shipping',
    # 'apps.tenant_apps.inventory',
    # 'apps.tenant_apps.suppliers',
    # 'shared.apps.nfe',
]
INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

# Configurações do Tenant
TENANT_MODEL = "tenants.Tenant"
TENANT_DOMAIN_MODEL = "tenants.Domain"
# Publico schema
PUBLIC_SCHEMA_NAME = 'public'

#  MIDDLEWARE E OUTRAS CONFIGURAÇÕES
MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware', # sempre em primeiro lugar de acordo com o próprio multi-tenant
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASE_ROUTERS = [
    'django_tenants.routers.TenantSyncRouter',
]

ROOT_URLCONF = 'config.urls'

# páginas web
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Para wsgi
WSGI_APPLICATION = 'config.wsgi.application'

# Password
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo' 
USE_I18N = True
USE_TZ = True

# Arquivos estáticos e mídia
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# para produção
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Storage para arquivos de mídia por tenant
DEFAULT_FILE_STORAGE = 'django.core.files.storage.TenantFileSystemStorage'

# Primary Key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SHOW_PUBLIC_IF_NO_TENANT_FOUND = True
TENANT_SUBFOLDER_PREFIX = None
SITE_ID = 1
