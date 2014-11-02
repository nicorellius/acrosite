"""
Django developer specific settings for acrosite project.

@date 2014-1026
@author nicorellius
"""

from .local import *



# set to tru for development
DEBUG = True

# secret key in local settings
with open('/home/nick/dev/prv/acros/secret_key.txt') as secret_key:
    SECRET_KEY = secret_key.read().strip()
    
# email smtp settings
with open('/home/nick/dev/prv/acros/email_password.txt') as email_password:
    EMAIL_PASSWORD = email_password.read().strip()
    
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD

INSTALLED_APPS += ('debug_toolbar',)