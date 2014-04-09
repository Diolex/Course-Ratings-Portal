#modules
from django.core.management.base import NoArgsCommand
import csv
import os
#models
#from courses.models import University, Department, Course, Section, Professor, Rating

class Command(NoArgsCommand):
    help = 'Populate database with information from csv files in $cwd/data/Lehigh Courses/'
    '''
    @param *args: required, but unused.
    @param **options: required, but unused at this time
    '''

    def handle(self, *args, **options):

        os.chdir("data/Lehigh Courses")
        total_courses = 0
        for dir_, _, files in os.walk(os.getcwd(), topdown=True):
            for fileName in files:
                relDir = os.path.relpath(dir_,os.getcwd())
                relFile = os.path.join(relDir, fileName)
                with open(relFile, 'r') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    rows = list(reader)
                    iter_row = iter(rows)
                    next(iter_row)
                    for row in iter_row:
                        self.save_course(row)
                    num_rows = len(rows)
                    total_courses += num_rows
                    print(num_rows,"courses read from",relFile)
        print("Total courses imported:",total_courses)
    def save_course(self, row):
        print(row)
        #Separate out course name, id, registration code, section id
