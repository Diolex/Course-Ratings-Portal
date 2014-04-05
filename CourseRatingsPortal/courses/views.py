from django.shortcuts import render_to_response
from courses.models import Professor

# Create your views here.
def index(request):
    if request.method == 'GET':
        print("GET called")
    return render_to_response('search_prof.html')

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

def search_course(request):
    return render_to_response('search_course.html')

def search_sections(request):
    return render_to_response('search_sections.html')

def initiate_prof_search(request):
    prof_listing = []
    args={}
    if 'name' in request.GET:
        args['name__contains']= request.GET.get('name')
    if 'department' in request.GET:
        args['department__dep_name__contains']= request.GET.get('name')
    if 'ratings' in request.GET:
        args['rating_value'] = request.GET.get('ratings')
    if 'quality' in request.GET:
        args['easiness_value'] = request.GET.get('quality')
    if 'easiness' in request.GET:
        args['easiness'] = request.GET.get('easiness')
    professors = Professor.objects.filter(**args)
    for professor in professors:
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

    return render('professor_results.html',prof_listing)

def initiate_course_search(request):
    course_listing = []
    args={}
    if 'name' in request.GET:
        args['course_name__contains']=request.GET.get('name')
    if 'course_id' in request.GET:
        args['course_id']=request.GET.get('course_id')
    if 'registration_code' in request.GET:
        args['registration_code']=request.GET.get('registration_code')
    if 'university' in request.GET:
        args['university__university_name__contains'] = request.GET.get('university')
    if 'department' in request.GET:
        args['department__contains'] = request.GET.get('department')
    if 'professor' in request.GET:
        args['professor__name__contains'] = request.GET.get('professor')

    courses = Course.objects.filter(**args)
    for course in courses:
        course_dict = {}
        course_dict['course_object'] = course
        course_dict['name'] = course.course_name
        course_dict['university'] = course.university.university_name
        course_dict['department'] = course.department.dep_name
        course_dict['professor'] = course.professor.name
        course_dict['registration_code'] = course.registration_code
        course_listing.append(course_dict)

    return render('course_results.html', course_listing)

