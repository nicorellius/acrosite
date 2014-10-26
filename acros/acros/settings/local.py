"""
Django local settings for acrosticshirts acrosite project.
"""

from .base import *

# set to `True` for development
DEBUG = True

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