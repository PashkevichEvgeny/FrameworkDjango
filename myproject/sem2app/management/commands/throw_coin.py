import random

from django.core.management.base import BaseCommand

from sem2app.models import Coin


class Command(BaseCommand):
    help = "Print Coin"

    def handle(self, *args, **kwargs):
        coin = Coin(side=random.randint(0, 1))
        coin.save()
        self.stdout.write(f'{coin}')
