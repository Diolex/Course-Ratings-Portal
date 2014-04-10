from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'CourseRatingsPortal.views.home'),
    url(r'^search/', include('search.urls')),
    url(r'^course/', include('courses.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),


)

