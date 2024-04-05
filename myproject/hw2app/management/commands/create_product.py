import random

from django.core.management.base import BaseCommand

from hw2app.models import Product


class Command(BaseCommand):
    help = 'Create Product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Enter name Product')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        r = random.randint(1, 50)
        product = Product.objects.create(name=name,
                                         description='Some description',
                                         price=r + 0.99,
                                         amount=r,)

        self.stdout.write(f'{product}')

            # Product.objects.create(name=f'prod_{i}',
            #                        description=f'description_{i}_for_prod_{i}',
            #                        price=i * 1.11,
            #                        amount=i * 5)
