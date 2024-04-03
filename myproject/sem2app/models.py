from django.db import models

# Create your models here.


class Coin(models.Model):
    """Задача 1"""
    side = models.BooleanField()
    throw_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name_side = 'Выпал ОРЕЛ' if self.side else 'Выпала РЕШКА'
        return f'{name_side}, время подбрасывания монеты {self.throw_time.__format__("%m-%d %H:%M")}'

