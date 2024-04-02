import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# - Орёл или решка
# - Значение одной из шести граней игрального кубика
# - Случайное число от 0 до 100
# - Пропишите маршруты


def head_tails(request):
    res = random.choice(['Орел', 'Решка'])
    return HttpResponse(f'На монетке - {res}!')


def dice(request):
    res = random.randint(1, 6)
    return HttpResponse(f'Вам выпало {res}!')


def rand100(request):
    return HttpResponse(random.randint(0, 100))
