from django.conf.urls import patterns, url
from search import views
from django.contrib import admin
admin.autodiscover()
urlpatterns=patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^professor/$', views.search_prof, name='professors'),
        url(r'^course/$', views.search_course, name='courses'),
        url(r'^professor/*', views.initiate_prof_search, name='professors_result'),
        url(r'^course/*',views.initiate_course_search, name='courses_result'),

)
