from django.conf.urls import patterns, include, url
from account import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.index),
        url(r'^edit_profile/$', views.edit_profile),
        url(r'^(?P<user>\w+)/$', views.get_profile),
)

