from django.shortcuts import render
from account.models import UserProfile

# Create your views here.


def account_home(request):
    return HttpResponse("Placeholder: User Home")

def edit_profile(request):
    return HttpResponse("Placeholder: Edit own profile")

def get_profile(request, user):
    return HttpResponse("Placeholder: View any user profile")
