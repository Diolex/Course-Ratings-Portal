from django.shortcuts import render_to_response
from courses.models import Professor

# Create your views here.
def search_prof_by_department(request, department_name):
    prof_listing = []

    for professor in Professor.objects.filter(
            department__dep_name__startswith = department_name):
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

    return render_to_response('search_prof_dep.html')
def search_prof(request):
    return render_to_response('search_prof.html')
