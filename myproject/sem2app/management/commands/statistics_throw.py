from django.core.management.base import BaseCommand

from sem2app.models import Coin


class Command(BaseCommand):
    help = "Statistics of coins throwing"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='Amount of coins')

    def handle(self, *args, **kwargs):
        n = kwargs['n']
        amount_coins = Coin.objects.count()
        # Sorry, у нас были три курса по SQL, разобратся с Queryset за пару часов не получилось
        query = Coin.objects.raw(f'SELECT * FROM sem2app_coin LIMIT {amount_coins - n}, {amount_coins}')
        heads = sum([i.side for i in query if i.side])
        d = {'Heads': heads, 'Tails': n - heads}
        self.stdout.write(f'{d}')
