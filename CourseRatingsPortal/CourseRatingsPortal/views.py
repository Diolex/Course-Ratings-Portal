from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib import admin
admin.autodiscover()
def home(request):
    return HttpResponseRedirect("/search/")
