from django.core.management.base import BaseCommand

from hw3app.models import Order, Product, Client


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Enter client id')
        parser.add_argument('product_ids', nargs='*', type=int, help='Enter products IDs')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        product_ids = kwargs['product_ids']
        if not (client_id := Client.objects.filter(pk=client_id).first()):
            self.stdout.write('Client not found')
        else:
            order = Order.objects.create(client_id=client_id)
            if product_ids:
                for product_id in product_ids:
                    if product := Product.objects.filter(pk=product_id).first():
                        order.products.add(product)
                        order.total_price += product.price
                order.save()
                product_in_order = "\n - ".join([str(i) for i in order.products.all()])
            else:
                product_in_order = 'No products added to order'
            self.stdout.write(f'{order}\nProducts add in order:\n - {product_in_order}')
