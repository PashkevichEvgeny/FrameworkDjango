from django.db import models


class Client(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name=}, {format(self.created, "%b %d %H:%M")}'


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk=} {self.name=} {self.price=} {self.amount=}'


class Order(models.Model):
    objects = None
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_order')
    products = models.ManyToManyField(Product, default=None, unique=False)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk=} {self.client_id.name} {self.total_price=}'

