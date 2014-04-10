from django.shortcuts import render_to_response
from courses.models import Course, Section, Professor
from django.db.models import Count
# Create your views here.
def index(request):
    if request.method == 'GET':
        print("GET called")
    return render_to_response('search/search_index.html')

def search_prof(request):
    return render_to_response('search/search_prof.html')

def search_course(request):
    return render_to_response('search/search_course.html')

def search_sections(request):
    return render_to_response('search/search_sections.html')

def initiate_prof_search(request):
    prof_listing = []
    args={}
    if request.GET.get('name'):
        args['name__contains']= request.GET.get('name')
    if request.GET.get('department'):
        args['department__dep_name__contains']= request.GET.get('department')
    if request.GET.get('ratings'):
        args['rating_value'] = request.GET.get('ratings')
    if request.GET.get('quality'):
        args['easiness_value'] = request.GET.get('quality')
    if request.GET.get('easiness'):
        args['easiness'] = request.GET.get('easiness')
    professors = Professor.objects.filter(**args)

    profs = []
    for prof in professors:
        profs.append(prof)
    dict = {"professors": profs}

    '''
    for professor in professors:
        prof_dict = {}
        prof_dict['professor_object'] = professor
        prof_dict['name']=professor.name
        prof_dict['university']=professor.university.university_name
        prof_dict['rating_value']=professor.rating_value
        prof_dict['easiness_value']=professor.easiness_value
        prof_dict['department']=[ x.dep_name for x in professor.department.all()]
        prof_listing.append(prof_dict)
    '''
    return render_to_response('search/professor_results.html',dict)

def initiate_course_search(request):
    course_listing = []
    args={}
    if request.GET.get('name'):
        args['course_name__contains']=request.GET.get('name')
    if request.GET.get('course_id'):
        args['course_id__contains']=request.GET.get('course_id')
    #if request.GET.get('registration_code'):
    #    args['registration_code']=request.GET.get('registration_code')
    if request.GET.get('university'):
        args['university__university_name__contains'] = request.GET.get('university')
    if request.GET.get('department'):
        args['department__contains'] = request.GET.get('department')
    #if request.GET.get('professor'):
    #    args['professor__name__contains'] = request.GET.get('professor')

    courses = Course.objects.filter(**args).annotate(section_cout = Count('section'))
    dict = {"courses" : courses}
    return render_to_response('search/courses_results.html', dict)

def course_handler(request, course_id):
    print(course_id)
    course = Course.objects.get(course_id=course_id)
    sections = Section.objects.filter(course__course_id=course_id)
    params = {'course':course, 'sections':sections }
    return render_to_response('search/course_sections.html', params)
