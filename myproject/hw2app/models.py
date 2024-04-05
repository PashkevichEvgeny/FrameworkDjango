from django.db import models

# Создайте три модели Django: клиент, товар и заказ.
# Клиент может иметь несколько заказов.
# Заказ может содержать несколько товаров.
# Товар может входить в несколько заказов.
# *Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе данных.


class Client(models.Model):
    """Поля модели "Клиент":
    - имя клиента
    - электронная почта клиента
    - номер телефона клиента
    - адрес клиента
    - дата регистрации клиента
    """
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name=}, {format(self.created, "%b %d %H:%M")}'


class Product(models.Model):
    """
    Поля модели "Товар":
    - название товара
    - описание товара
    - цена товара
    - количество товара
    - дата добавления товара
    """
    objects = None
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk=} {self.name=} {self.price=} {self.amount=}'


class Order(models.Model):
    """
    ## Домашнее задание
    Поля модели "Заказ":
    - связь с моделью "Клиент", указывает на клиента, сделавшего заказ
    - связь с моделью "Товар", указывает на товары, входящие в заказ
    - общая сумма заказа
    - дата оформления заказа
    """
    objects = None
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_order')
    products = models.ManyToManyField(Product, default=None, unique=False)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk=} {self.client_id.name} {self.total_price=}'
