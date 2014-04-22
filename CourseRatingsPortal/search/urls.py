from django.conf.urls import patterns, url
from search import views
from courses import views as course_views
from django.contrib import admin
admin.autodiscover()
urlpatterns=patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^professor/$', views.search_prof, name='professors'),
        url(r'^course/$', views.search_course, name='courses'),
        url(r'^sections/(?P<course_id>[\w+\ +]*)', views.course_handler),
        url(r'^professor/*', views.initiate_prof_search, name='professors_result'),
        url(r'^course*',views.initiate_course_search, name='courses_result'),
        url(r'^create/professor$', course_views.ProfessorCreate.as_view(success_url="/search/"), name='professor_create'),
        url(r'^create/course$', course_views.CourseCreate.as_view(success_url="/search/"), name='course_create'),
        url(r'^create/university$', course_views.UniversityCreate.as_view(success_url="/search/"), name='university_create'),
        url(r'^create/section$', course_views.SectionCreate.as_view(success_url="/search/"), name='section_create'),
        url(r'^create/rating$', course_views.RatingCreate.as_view(success_url="/search/"), name='rating_create'),
        url(r'^create/department$', course_views.DepartmentCreate.as_view(success_url="/search/"), name='department_create'),

)
