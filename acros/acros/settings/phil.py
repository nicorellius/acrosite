'''
developer-specific settings for phil.
Created on Oct 28, 2014

@author: phillipseitzer
'''

from .local import *

# set to true for development
DEBUG = True

# secret key in local settings
with open('/Users/phillipseitzer/dev/prv/acrosticshirts/secret_key.txt') as secret_key:
    SECRET_KEY = secret_key.read().strip()
    
# email smtp settings
with open('/Users/phillipseitzer/dev/prv/acrosticshirts/email_password.txt') as email_password:
    EMAIL_PASSWORD = email_password.read().strip()
    
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD