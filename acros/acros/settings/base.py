"""
Django settings for acrosite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

# gives the root of the project
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

# gives the path of the settings module
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# we could go full names, eg, pro, or just casual
ADMINS = (
    ('nick', 'nicorellius@gmail.com'),
    ('jimar', 'jeemar@gmail.com'),
    ('phil', 'phillipseitzer@gmail.com'),
)

MANAGERS = ADMINS

# set before deployment to dev test and production
ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    # Required by allauth template tags
    'django.core.context_processors.request',
    # allauth specific context processors
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# allauth configuration
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'

"""
site id for main site. This should be changed it deploying to development or production
see sites in admin, and change domain name to match the server name
"""
SITE_ID = 1

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'apps.accounts',
    'apps.generator',
    'apps.logs',
    'localflavor',
    # allauth registration and providers
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.facebook',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'acros.urls'

WSGI_APPLICATION = 'acros.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
