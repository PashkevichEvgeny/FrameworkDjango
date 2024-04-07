import random

from django.core.management.base import BaseCommand

from hw3app.models import Product


class Command(BaseCommand):
    help = 'Create Product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Enter name Product')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        r = random.randint(1, 50)
        product = Product.objects.create(name=name,
                                         description=f'Some {name} description.',
                                         price=r + 0.99,
                                         amount=0)

        self.stdout.write(f'{product}')
