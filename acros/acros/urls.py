"""
file        :   urls.py
date        :   2014-1026
module      :   acros
classes     :   
description :   main URLConf for acrosite
"""

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from common.sitemaps import SitePageSitemap, SiteFlatPageSitemap

from django.contrib import admin

from apps.generator.views import GenerateAcrosticFormView
from apps.generator.views import GenerateAcrosticSuccessView
from apps.generator.views import RateAcrosticView


sitemaps = {
    'flatpages': SiteFlatPageSitemap,
    'pages': SitePageSitemap(['index', ]),
}


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('allauth.urls')),

    # main page index
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),

    # acrostic viewer
    url(r'^generate/$', GenerateAcrosticFormView.as_view(), name='generate_acrostic_form_view'),
    url(r'^generate/acrostic/$', GenerateAcrosticSuccessView.as_view(), name='generate_acrostic_success_view'),
    url(r'^acrostic/rate/$', RateAcrosticView.as_view(), name='rate_acrostic_view'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)
