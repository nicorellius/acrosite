"""
file        :   urls.py
date        :   2014-1026
module      :   acros
classes     :   
description :   main URLConf for acrosite
"""

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

from apps.generator.views import GenerateAcrosticFormView
from apps.generator.views import GenerateAcrosticSuccessView
from apps.generator.views import RateAcrosticView

# This goes in the production urls.py
from acros.settings import production


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^accounts/', include('allauth.urls')),

    # main page index
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    # acrostic viewer
    url(r'^generate/$', GenerateAcrosticFormView.as_view(), name='generate_acrostic_form_view'),
    url(r'^generate/acrostic/$', GenerateAcrosticSuccessView.as_view(), name='generate_acrostic_success_view'),
    url(r'^acrostic/rate/$', RateAcrosticView.as_view(), name='rate_acrostic_view'),

    # This goes in the production urls.py
    # static file mappings
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': production.STATIC_ROOT,
    }),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': production.MEDIA_ROOT,
    }),
)
