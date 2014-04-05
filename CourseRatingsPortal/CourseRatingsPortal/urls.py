from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CourseRatingsPortal.views.home', name='home'),
    url(r'^search/', include('search.urls')),
    url(r'^courses/', include('course.urls')),
    #url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/professor/dep/(?P<department_name>[^/]+)/$', 'courses.views.search_prof_by_department'),


)

