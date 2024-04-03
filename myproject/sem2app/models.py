from django.db import models

# Create your models here.


class Coin(models.Model):
    """Задача 1"""
    objects = None
    side = models.BooleanField()
    throw_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name_side = 'Выпал ОРЕЛ' if self.side else 'Выпала РЕШКА'
        return f'{name_side}, время подбрасывания монеты {format(self.throw_time, "%m-%d %H:%M")}'

    # def __repr__(self):
    #     return f'Coin({self.side=}, {self.throw_time=})'
