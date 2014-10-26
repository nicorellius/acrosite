"""
Django local settings for acrosticshirts acrosite project.
"""

from .base import *

# set to tru for development
DEBUG = False

DATABASES = {
    # configure postgresql for production
}

# static and media files

STATICFILES_DIRS = (
    PROJECT_ROOT.child('static'),
    '/var/www/acros/static',
)

MEDIA_ROOT = '/var/www/acros/media'

STATIC_ROOT = '/var/www/acros/static'
