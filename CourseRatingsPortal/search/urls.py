from django.conf.urls import patterns, url
from search import views

urlpatterns=patterns('',
        url(r'^$', views.index, name='index'),
        url(r'professor/$', views.search_prof),
        url(r'course/$', views.search_course),
        url(r'professor/*', views.initiate_prof_search),
        url(r'course/*',views.initiate_course_search),

)
