"""
Django settings for mooder project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if os.path.exists(os.path.join(BASE_DIR, '.secretkey')):
    with open(os.path.join(BASE_DIR, '.secretkey'), 'rb') as f:
        SECRET_KEY = f.read()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_markup',
    'pure_pagination',
    'bootstrap3',
    'captcha',
    'accounts',
    'archives',
    'managements',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mooder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'mooder.context.global_site_context',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mooder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Mailgun api
EMAIL_HOST_USER = 'no-reply@example.com'
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = 'mailgun-api-key'
MAILGUN_SERVER_NAME = 'example.com'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mooder', 'static_cdn')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mooder', 'media_cdn')

AUTH_USER_MODEL = 'accounts.Member'

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('archive:index')

# MARKDOWN_DEUX_STYLES = {
#     "default": {
#         "extras": {
#             "code-friendly": None,
#             "fenced-code-blocks": None,
#             "break-on-newline": None
#         },
#         "safe_mode": "escape",
#     },
# }

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

MARKUP_SETTINGS = {
    'markdown': {
        'safe_mode': 'escape',
        'extensions': ('extra', 'nl2br', 'codehilite')
    }
}

USER_LEVEL_RANGE = (
    ((0, 30), ('anonymous', '路人甲'), 'default'),
    ((30, 100), ('practice', '见习白帽子'), 'secondary'),
    ((100, 300), ('general', '正式白帽子'), 'primary'),
    ((300, 1000), ('senior', '高级白帽子'), 'success'),
    ((1000, 2000), ('supreme', '核心白帽子'), 'warning'),
    ((2000, -1), ('god', '妇科圣手'), 'danger')
)

SITE = {
    'title': 'BlueCat 团队漏洞交流平台（内部使用）',
    'description': '内部使用的漏洞交流平台',
    'keyword': 'bluecat,安全,团队,贡献,SRC,XSS,CTF'
}

ACCOUNT_ACTIVATION_DAYS = 3
REGISTRATION_AUTO_LOGIN = False
INCLUDE_AUTH_URLS = False
INCLUDE_REGISTER_URL = True
REGISTRATION_FORM = 'accounts.forms.SignupForm'

# 是否启用邮箱激活，False则需要管理员手工激活，True为邮箱激活
SEND_ACTIVATION_EMAIL = True

INTERNAL_IPS = ['127.0.0.1']
