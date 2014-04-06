from django.core.management.base import NoArgsCommand
from courses.models import Rating, Professor, Course, Section
class Command(NoArgsCommand):
    help = 'Process all new ratings for courses and professors, then update their values'

    def handle(self, *args, **options):
        self.stdout.write("Processing ratings.");

