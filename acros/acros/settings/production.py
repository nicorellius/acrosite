"""
Django production settings for acrosite project.
"""

from .base import *

# set to `false` for production
DEBUG = False

# secret key in local settings
with open('/home/dev/prv/acros/secret_key.txt') as secret_key:
    SECRET_KEY = secret_key.read().strip()

# email smtp settings
with open('/home/dev/prv/acros/email_password.txt') as email_password:
    EMAIL_PASSWORD = email_password.read().strip()

EMAIL_HOST_PASSWORD = EMAIL_PASSWORD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}

# email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'acrostic.mail@gmail.com'
# this password is meant to be over-ridden in `settings/<devs_name>.py`
# eg, set EMAIL_HOST_PASSWORD = EMAIL_PASSWORD after reading password from file
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '587'
EMAIL_USE_TLS = True


"""
For databases, https://docs.djangoproject.com/en/1.7/ref/settings/#databases
PostgreSQL database setting
"""
"""
with open('/path/to/db_password.txt') as db_password:
    DB_PASSWORD = db_password.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': DB_PASSWORD
        'HOST': '',
        'PORT': '',
    }
}
"""

MEDIA_ROOT = '/var/www/acros/media'

STATIC_ROOT = '/var/www/acros/static'

# set before deployment to dev test and production
ALLOWED_HOSTS = ['ecrostic.com', 'www.ecrostic.com', 'dev.ecrostic.com']

TEMPLATE_DIRS = (
    '/home/dev/django/projects/acrosite/acros/templates'
)
