"""
file        :   context_processors.py
date        :   2015-0302
module      :   common
classes     :   
description :   template context processors
"""

from django.contrib.sites.models import get_current_site
from django.utils.functional import SimpleLazyObject


def get_url(request):

    site = SimpleLazyObject(lambda: get_current_site(request))
    protocol = 'https' if request.is_secure() else 'http'

    return {
        'site': site,
        'site_root': SimpleLazyObject(lambda: "{0}://{1}".format(protocol, site.domain)),
    }

# http://stackoverflow.com/questions/1451138
# from django.conf import settings
# def site(request):
#     return { 'SITE_URL': settings.SITE_URL }