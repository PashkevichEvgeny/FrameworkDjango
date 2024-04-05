from django.core.management.base import BaseCommand

from hw2app.models import Order, Product, Client


class Command(BaseCommand):
    help = 'Add products in order'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Enter order id')
        parser.add_argument('product_ids', nargs='*', type=int, help='Product IDs')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        product_ids = kwargs['product_ids']
        if (order := Order.objects.filter(pk=order_id).first()) and product_ids:
            for product_id in product_ids:
                if (product := Product.objects.filter(pk=product_id).first()) and order.products.contains(product):
                    order.total_price -= product.price
                    order.products.remove(product)
                    order.save()
                    self.stdout.write(f'{product.name} удален из заказа')
                else:
                    self.stdout.write('Product not found')
            self.stdout.write(f'{order.total_price= } {order.products.all()}')