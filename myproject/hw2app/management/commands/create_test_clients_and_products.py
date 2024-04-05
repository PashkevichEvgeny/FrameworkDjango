from django.core.management.base import BaseCommand

from hw2app.models import Client, Product


class Command(BaseCommand):
    help = 'Create clients'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='Enter number clients')

    def handle(self, *args, **options):
        n = options['n']
        for i in range(1, n + 1):
            Client.objects.create(name=f'name_{i}',
                                  email=f'name_{i}@gmail.com',
                                  phone=str(i) * 12,
                                  address=f'City_{i}, Street_{i}',)
            Product.objects.create(name=f'prod_{i}',
                                   description=f'description_{i}_for_prod_{i}',
                                   price=i * 1.11,
                                   amount=i * 5)

        self.stdout.write(f'{n} Clients and Products are created')
