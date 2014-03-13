from django.shortcuts import render
from courses.models import Professor, Department

# Create your views here.
def search_prof_by_department(request, department_name):
    prof_listing = []

    for professor in Professor.objects.filter():#how to filter this?
        prof_dict = {}
        prof_dict['professor_object'] = professor
        prof_dict['first_name']= professor.first_name
        prof_dict['middle_name']=professor.middle_name
        prof_dict['last_name']=professor.last_name
        prof_dict['university']=professor.university.university_name
        prof_dict['rating_value']=professor.rating_value
        prof_dict['easiness_value']=professor.easiness_value
        prof_dict['department']=professor.department.dep_name
        prof_listing.append(prof_dict)

    return
