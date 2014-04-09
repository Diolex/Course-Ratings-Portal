from django.shortcuts import render
from django.http import HttpResponse
from courses.models import University, Department, Professor, Course, Section, Rating


# Create your views here.
def index(request):
    return HttpResponse("Course index - redirect to course search page")

def get_course(request, university, course):
    qs_course = Course.objects.filter(university__university_name__contains=university).filter(course_id__contains=course)

    return HttpResponse("Display page - University: "+university+", Course:"+course)

def get_professor(request, university, professor):
    qs_professor = Professor.objects.filter(university__university_name__contains=university).filter(name__contains=professor)

    return HttpResponse("Display page- Universit: "+university+", Professor:"+professor)
