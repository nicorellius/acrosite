"""
Django local settings for acrosticshirts acrosite project.
"""

from .base import *

# secret key in local settings
with open('/home/nick/dev/prv/acros/secret_key.txt') as secret_key:
    SECRET_KEY = secret_key.read().strip()

# set to tru for development
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),     	
    }
}

# email smtp settings
with open('/home/nick/dev/prv/acros/email_password.txt') as email_password:
    EMAIL_PASSWORD = email_password.read().strip()

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'acrostic.mail@gmail.com'
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
EMAIL_PORT = '587'
EMAIL_USE_TLS = True