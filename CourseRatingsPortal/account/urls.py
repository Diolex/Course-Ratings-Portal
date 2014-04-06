from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from account import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^user/$', views.account_home),
        url(r'^user/edit_profile/$', views.edit_profile),
        url(r'^user/view/\w{0,50}', views.get_profile),
)

