from django.conf.urls import patterns, url
from courses import views
from search import views as search
from django.contrib import admin
admin.autodiscover()
urlpatterns=patterns('',
        url(r'^/create$', views.CourseCreate.as_view(), name='course_create'),
        url(r'^$', views.index),
        url(r'^(?P<university>\w+)/(?P<course>\w+)\$', views.get_course), #university, course_name
        url(r'^/professor/(?P<university>\w+)/(?P<professor>\w+)\$', views.get_professor),
        url(r'^/professor/create', views.ProfessorCreate.as_view(success_url="/search/")),
        url(r'^/university/create\$', views.UniversityCreate.as_view(success_url="/search/"), name='university_create'),
        url(r'^/department/create\$', views.DepartmentCreate.as_view(success_url="/search/"), name='department_create'),
        url(r'^/section/create\$', views.SectionCreate.as_view(success_url="/search/"), name='section_create'),
        url(r'^/course/(?P<course_id>\d+)\$', search.course_handler),
        url(r'^/rating/create\$', views.RatingCreate.as_view(success_url="/search/"), name='rating_create'),
)

