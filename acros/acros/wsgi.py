"""
WSGI config for acros project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/home/dev/virtualenv/acrosite/lib/python3.3/site-packages/')

sys.path.append('/home/dev/django/projects/acrosite/acros')
sys.path.append('/home/dev/django/projects/acrosite/acros/acros')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acros.settings.production")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
