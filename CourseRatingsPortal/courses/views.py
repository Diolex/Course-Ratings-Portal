from django.shortcuts import render
from django.http import HttpResponse
from courses.models import University, Department, Professor, Course, Section, Rating


# Create your views here.
def index(request):
    return HttpResponse("Course index - redirect to course search page")

def get_course(request, university, course):
    return HttpResponse("Display page - University: "+university+", Course:"+course)
