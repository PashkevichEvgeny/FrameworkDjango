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

    def __repr__(self):
        return f'Coin({self.side=}, {self.throw_time=})'


class Author(models.Model):
    """## Задание №3
    Создайте модель Автор.
    Модель должна содержать следующие поля:
    - имя до 100 символов
    - фамилия до 100 символов
    - почта
    - биография
    - день рождения
    Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
    """
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    dob = models.DateField()

    def full_name(self):
        return f'{self.name} {self.surname}'
