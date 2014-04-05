from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = 'Expires searches which are older than the set number of hours'

    def handle(self, *args, **options):
        self.stdout.write("This method should expire searches after "+args[0]+" hours");

