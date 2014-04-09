from django.core.management.base import NoArgsCommand
import csv

from courses.models import *

class Command(NoArgsCommand):
    help = 'Populate database with information from csv files'
    '''
    @param *args:  accepts one argument- path to folder containing csv files, or path of csv file to process
    @param **options:  acceptable options: iscsv=true or iscsv=false (interpret path as csv or folder)
    '''
    def handle(self, *args, **options):
        for arg in args:
            print(arg)

