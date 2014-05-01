#modules
from django.core.management.base import NoArgsCommand
import json
import os
import re

#models
from courses.models import University, Department, Professor, Rating


class Command(NoArgsCommand):
    help = 'Populate database with information from csv files in $cwd/data/Lehigh Courses/'
    '''
    @param *args: arg1 = path to folder containing files, arg2 = univeristy_name
    @param **options: required, but unused at this time
    '''

    def handle(self, *args, **options):
        university_name = ''
        if len(args)!=2:
            os.chdir("data/Lehigh Professors/")
            university_name='Lehigh University'
        else:
            os.chdir("args[0]")
            university_name=args[1]

        u_set = University.objects.filter(university_name=university_name)
        if len(u_set)==0:
            print("Creating university:",university_name)
            u = University(university_name=university_name)
            u.save()
            u_set= University.objects.filter(university_name=university_name)
        university=u_set[0]

        totals = [0,0] #professors, ratings

        json_data = open("profs.json").read()
        data = json.loads(json_data)

        for rating in data:
            prof_name = rating['Name']
            split_name = prof_name.split(", ")
            list.reverse(split_name)
            full_name = " ".join(split_name)
            quality = 0
            easiness = 0
            if int(rating['Ratings'])!=0:
                quality = float(rating['Quality2'])
                easiness = float(rating['Easiness'])
            professor = Professor.objects.filter(name=full_name)
            newprof = False
            if not professor:
                new_professor = Professor(name = full_name, university=university)
                new_professor.save()
                professor=new_professor
                totals[0]+=1
                newprof = True
            else:
                professor = professor[0]
                Rating.objects.filter(professor=professor).delete()
                new_rating = Rating(professor = professor, rating_text="Imported", rating_quality=quality, rating_easiness=easiness)
                new_rating.save()
                totals[1]+=1
            print("Imported: {0} rating. New professor: {1}".format(professor.name, newprof))
        print("{0} professors and {1} ratings read".format(*totals))
