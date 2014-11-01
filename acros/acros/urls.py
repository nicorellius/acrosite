"""
file        :   urls.py
date        :   2014-1026
module      :   acros
classes     :   
desription  :   main URLConf for acrosite
"""


from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

from apps.generator.views import GenerateAcrosticFormView, GenerateAcrosticSuccessView

admin.autodiscover()

urlpatterns = patterns('',

    # admin
    url(r'^admin/', include(admin.site.urls)),
    
    # main page index
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    
    # acrostic veiwer
    url(r'^generate/$', GenerateAcrosticFormView.as_view(), name='generate_acrostic_form_view'),
    url(r'^generate/success/$', GenerateAcrosticSuccessView.as_view(), name='generate_acrostic_success_view'),
    
)