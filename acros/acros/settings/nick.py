"""
file        :   nick.py
date        :   2014-10-26
module      :   settings
classes     :
description :   Nick-specific development settings
"""

from .local import *

# set to True for development
DEBUG = True

# secret key in local settings
with open('/home/nick/dev/prv/acros/secret_key.txt') as secret_key:
    SECRET_KEY = secret_key.read().strip()
    
# email smtp settings
with open('/home/nick/dev/prv/acros/email_password.txt') as email_password:
    EMAIL_PASSWORD = email_password.read().strip()
    
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD

INSTALLED_APPS += (
    'debug_toolbar',
    'sslserver',
    'apps.search'
)

from django.conf.locale.en import formats as en_formats
en_formats.DATETIME_FORMAT = "Y-m-d, H:i:s"