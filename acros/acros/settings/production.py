"""
Django production settings for acrosite project.
"""

from .base import *

# set to False for production
DEBUG = False

# for databases, https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# postgresql database setting
#with open('/path/to/db_password.txt') as db_password:
#    DB_PASSWORD = db_password.read().strip()

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': '',
#        'USER': '',
#        'PASSWORD': DB_PASSWORD
#        'HOST': '',
#        'PORT': '',
#    }
#}

# static and media files
STATICFILES_DIRS = (
    PROJECT_ROOT.child('static'),
    '/var/www/acros/static',
)

MEDIA_ROOT = '/var/www/acros/media'

STATIC_ROOT = '/var/www/acros/static'
