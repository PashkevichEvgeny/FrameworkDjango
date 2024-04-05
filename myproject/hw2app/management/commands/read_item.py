from django.core.management import BaseCommand

from hw2app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Read items from selected table'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Enter name item')
        parser.add_argument('item_id', nargs='+', type=int, help='List IDs, 0 for All')

    def handle(self, *args, **kwargs):
        tables = {'client': Client, 'product': Product, 'order': Order}
        name = kwargs['name']
        pks = kwargs['item_id']
        for pk in pks:
            if pk == 0:
                items = tables[name].objects.all()
                str_items = '\n'.join([str(item) for item in items])
                self.stdout.write(str_items)
            elif item := tables[name].objects.filter(pk=pk).first():
                self.stdout.write(f'{item}')
            else:
                self.stdout.write('No found!')