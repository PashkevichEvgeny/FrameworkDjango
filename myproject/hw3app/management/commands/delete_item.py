from django.core.management import BaseCommand

from hw3app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Delete items from selected table'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Enter name item')
        parser.add_argument('item_id', nargs='+', type=int, help='List IDs')

    def handle(self, *args, **kwargs):
        tables = {'client': Client, 'product': Product, 'order': Order}
        name = kwargs['name']
        pks = kwargs['item_id']
        for pk in pks:
            if item := tables[name].objects.filter(pk=pk).first():
                self.stdout.write(f'{item}')
                item.delete()
            else:
                self.stdout.write('No found!')