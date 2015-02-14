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
)

from django.conf.locale.en import formats as en_formats
en_formats.DATETIME_FORMAT = "Y-m-d, H:i:s"

# # nick's logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'log_file': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             # 'filename': '/home/nick/dev/django/projects/acrosite/acros/apps/logs/debug.log',
#             'filename': os.path.join(PROJECT_ROOT, 'apps/logs/debug.log'),
#             'maxBytes': 16777216,
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['log_file'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#         'django.request': {
#             'handlers': ['console', 'log_file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'apps.generator': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     },
# }