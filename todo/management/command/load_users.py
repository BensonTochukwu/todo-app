from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load user fixtures'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'users.json')
        self.stdout.write(self.style.SUCCESS('Users loaded successfully!'))
