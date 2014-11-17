"""
Django developer specific settings for acrosite project.

2014-1026
nicorellius
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

#INSTALLED_APPS += ('debug_toolbar',)
#
#DEBUG_TOOLBAR_CONFIG = {
#    'INSERT_BEFORE': '<span id="insert-debug-toolbar"></span>',
#    'JQUERY_URL': '',
#}
#
#INTERNAL_IPS = (
#    '127.0.0.1',
#)
