from django.core.management.base import BaseCommand

from sem2app.models import Author


class Command(BaseCommand):
    help = "Create Post"

    # def add_arguments(self, parser):
    #     parser.add_argument('n', type=int, help='Amount of coins')

    def handle(self, *args, **kwargs):
        d = {'name': 'Нельсон',
             'surname': 'Мандела',
             'email': 'mandela@mandela.com',
             'biography': 'https://en.wikipedia.org/wiki/Nelson_Mandela',
             'dob': '1918-07-18'}
        post = Author(**d)
        post.save()
        self.stdout.write(f'{post}')
