from django.db import models

# Create your models here.


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    image = models.ImageField(default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk=} {self.name=} {self.price=} {self.amount=}'
