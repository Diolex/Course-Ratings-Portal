#modules
from django.core.management.base import NoArgsCommand
import csv
import os
import re
#models
from courses.models import University, Department, Course, Section, Professor, Rating

class Command(NoArgsCommand):
    help = 'Populate database with information from csv files in $cwd/data/Lehigh Courses/'
    '''
    @param *args: arg1 = path to folder containing files, arg2 = univeristy_name
    @param **options: required, but unused at this time
    '''

    def handle(self, *args, **options):
        university_name=''
        if len(args)!=2:
            os.chdir("data/Lehigh Courses")
            university_name='Lehigh University'
        else:
            os.chdir(args[0])
            university_name = args[1]
        total_courses = 0

        #make sure university exists. If not, create it
        u_set = University.objects.filter(university_name=university_name)
        if len(u_set)==0:
            print("Creating university:",university_name)
            u = University(university_name=university_name)
            u.save()
            u_set= University.objects.filter(university_name=university_name)
        university = u_set[0]
        for dir_, _, files in os.walk(os.getcwd(), topdown=True):
            for fileName in files:
                relDir = os.path.relpath(dir_,os.getcwd())
                relFile = os.path.join(relDir, fileName)
                print("Beginning to read",fileName)
                #make sure department exists. If not, create it
                dep_name = fileName[:len(fileName)-4]
                d_set = Department.objects.filter(dep_name =dep_name)
                if len(d_set)==0:
                    d = Department(dep_name = dep_name)
                    d.save()
                    d_set = Department.objects.filter(dep_name=dep_name)
                department = d_set[0]

                #open file and begin saving courses
                with open(relFile, 'r') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    rows = list(reader)
                    iter_row = iter(rows)
                    next(iter_row)
                    for row in iter_row:
                        self._save_course(row,university,department)
                    num_rows = len(rows)
                    total_courses += num_rows
                    print(num_rows,"courses read from",relFile)
        print("Total courses imported:",total_courses)
    def _save_course(self, row, university, department):
        #Separate out course name, id, registration code, section id
        course_listing = row[0]
        p = re.compile(r'\s-\s')
        split = p.split(course_listing)

        #construct course
        c_set = Course.objects.filter(course_id=split[2], course_name=split[0],
                university=university, department=department)
        if len(c_set)==0:
            new_course = Course(course_id = split[2], course_name=split[0],
                    university=university, department=department)
            new_course.save()
            print("Created Course:",new_course.course_id,new_course.course_name)
            c_set = Course.objects.filter(course_id=split[2], course_name=split[0],
                    university=university, department=department)
        course = c_set[0]
        has_secondary = len(row)>=14
        #check if professor exists
        prof_names = row[7].split(',')
        prof_names[0] = prof_names[0][:len(prof_names[0])-3]
        prof_names = [ ' '.join(s.split()) for s in prof_names]
        prof_names2=[]
        if has_secondary is True:
            prof_names2=row[14].split(',')
            prof_names2[0]=prof_names2[0][:len(prof_names2[0])-3]
            prof_names2=[' '.join(s.split()) for s in prof_names2]
        profs=[]
        for prof_name in prof_names:
            p_set = Professor.objects.filter(university=university,name=prof_name)
            if len(p_set)==0:
                new_professor = Professor(name=prof_name, university=university)
                new_professor.save()
                profs.append(new_professor)
                print('Created Professor:',prof_name,university.university_name)
            else:
                profs.extend(p_set)
        profs2=[]
        for prof_name in prof_names2:
            p_set = Professor.objects.filter(university=university,name=prof_name)
            if len(p_set)==0:
                new_professor = Professor(name=prof_name, university=university)
                new_professor.save()
                profs2.append(new_professor)
        profs=[]
        for prof_name in prof_names:
            p_set = Professor.objects.filter(university=university,name=prof_name)
            if len(p_set)==0:
                new_professor = Professor(name=prof_name, university=university)
                new_professor.save()
                profs.append(new_professor)
                print('Created Professor:',prof_name,university.university_name)
            else:
                profs.extend(p_set)
        for prof in profs2:
            prof.department.add(department)

        s_set = Section.objects.filter(course=course,section_id=split[3],
                registration_code=split[1])
        if len(s_set)==0:
            new_section = Section(course=course, section_id=split[3], registration_code=split[1],
                    time = row[2], days=row[3], location=row[4], date_range = row[5],
                    schedule_type = row[6], schedule_type2 = row[8] if has_secondary else '',
                    time2 = row[9] if has_secondary else '', days2 = row[10] if has_secondary else '',
                    location2 = row[11] if has_secondary else '', date_range2 = row[12] if has_secondary else '')
            new_section.save()
            for prof in profs:
                new_section.professor.add(prof)
            for prof in profs2:
                new_section.professor.add(prof)

            new_section.save()
            print('Created Section:',course.course_id,new_section.section_id)


