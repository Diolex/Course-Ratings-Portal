from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import admin
admin.autodiscover()
def index(request):
    return HttpResponse("Course Ratings Portal Home Page")
