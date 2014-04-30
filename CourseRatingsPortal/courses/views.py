from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView#, UpdateView
from django.forms import ModelForm
from django.http import HttpResponse
from courses.models import University, Department, Professor, Course, Section, Rating


# Create your views here.
def index(request):
    return HttpResponse("Course index - redirect to course search page")

def get_course(request, university, course):
    qs_course = Course.objects.filter(university__university_name__contains=university).filter(course_id__contains=course)
    return render_to_response("university_display.html",qs_course)
    #return HttpResponse("Display page - University: "+university+", Course:"+course)

def get_professor(request, university, professor):
    qs_professor = Professor.objects.filter(university__university_name__contains=university).filter(name__contains=professor)
    return render_to_response("professor_display.html",qs_professor)
    #return HttpResponse("Display page- Universit: "+university+", Professor:"+professor)


class UniversityCreate(CreateView):
    model = University
    fields = ['university_name']

class DepartmentCreate(CreateView):
    model = Department
    fields = ['dep_name']

class ProfessorCreate(CreateView):
    model = Professor
    fields = ['name', 'rating_value', 'university', 'department']

class CourseCreate(CreateView):
    model = Course
    fields = ['course_id', 'course_name', 'university', 'department']

class SectionCreate(CreateView):
    model = Section
    fields = ['course', 'section_id', 'registration_code', 'professor', 'location', 'location2',
              'class_type', 'class_type2', 'time', 'time2', 'days', 'days2', 'date_range',
              'date_range2', 'schedule_type', 'schedule_type2']

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ('course','counted','date_created','date_modified')

class RatingCreate(CreateView):
    form_class = RatingForm
    model = Rating
    fields = ['course', 'professor', 'rating_text', 'rating_quality', 'rating_easiness', 'counted']
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(RatingCreate, self).form_valid(form)
