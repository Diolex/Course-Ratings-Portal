from django.conf.urls import patterns, url
from courses import views

from django.contrib import admin
admin.autodiscover()
urlpatterns=patterns('',
        url(r'^$', views.index),
        url(r'^(?P<university>\w+)/(?P<course>\w+)\$', views.get_course), #university, course_name
        url(r'^/professor/(?P<university>\w+)/(?P<professor>\w+)\$', views.get_professor),
        url(r'^/professor/create\$', views.ProfessorCreate.as_view(), name='professor_create'),
        url(r'^/university/create\$', views.UniversityCreate.as_view(), name='university_create'),
        url(r'^/department/create\$', views.DepartmentCreate.as_view(), name='department_create'),
        url(r'^/course/create\$', views.CourseCreate.as_view(), name='course_create'),
        url(r'^/section/create\$', views.SectionCreate.as_view(), name='section_create'),
        url(r'^/rating/create\$', views.RatingCreate.as_view(), name='rating_create'),
)

