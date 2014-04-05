from django.conf.urls import patterns, url
from courses import views

urlpatterns=patterns('',
        url(r'^$', views.index, name='index'),
        url(r'professor/department/', views.search_prof_by_department, name='professor search by department'),
)
