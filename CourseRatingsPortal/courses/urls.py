from django.conf.urls import patterns, url
from courses import views

from django.contrib import admin
admin.autodiscover()
urlpatterns=patterns('',
        url(r'^$', views.index),
        url(r'^(?P<university>\w+)/(?P<course>\w+)\$', views.get_course), #university, course_name
)

