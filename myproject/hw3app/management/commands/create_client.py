from django.core.management.base import BaseCommand

from hw3app.models import Client, Product


class Command(BaseCommand):
    help = 'Create client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Enter name client')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        client = Client.objects.create(name=name,
                                       email=f'{name}@gmaol.com',
                                       phone='000000000',
                                       address=f'{name.title()} City',)

        self.stdout.write(f'{client}')
