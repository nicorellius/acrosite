from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # admin
    url(r'^admin/', include(admin.site.urls)),
    
    # main page index
    url(r'^$', TemplateView.as_view(template_name="index.html")),
)