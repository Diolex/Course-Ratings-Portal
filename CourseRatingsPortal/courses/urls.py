from django.conf.urls import patterns, url
from courses import views

from django.contrib import admin
admin.autodiscover()
urlpatterns=patterns('',
        #url(r'^$', views.index),
        #url(r'^\w{1,50}/\w', views.get_course_info), #university, course_name
)

