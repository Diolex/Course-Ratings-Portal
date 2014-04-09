from django.shortcuts import render
from django.http import HttpResponse
from account.models import UserProfile

# Create your views here.


def index(request):
    return HttpResponse("Placeholder: account index")

def edit_profile(request):
    return HttpResponse("Placeholder: Edit own profile")

def get_profile(request, user):
    return HttpResponse("Placeholder: View "+user+"'s profile")

def login(request):
    return HttpResponse("This should be a login form")
