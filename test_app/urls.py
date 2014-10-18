# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from appp.models import Person

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hello/', 'appp.views.hello', name='hello'),
    url(r'^now/', 'appp.views.get_now', name='now'),
    url(r'^hours/$', 'appp.views.get_now', name='hours'),
    url(r'^hours/(\d{1,2})/$', 'appp.views.get_now_ahead', name='hours'),
    url(r'^$', 'appp.views.get_main', name='main'),
    url(r'^person_edit/$', 'appp.views.get_person_edit', name='person_edit'),
    url(r'^persons/$', ListView.as_view(model=Person), name='persons'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
