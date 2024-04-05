import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

# view as a function
def main(request):
    context = {"name": "John"}
    return render(request, "sem3app/index.html", context)


# view as a class
class TemplateAbout(TemplateView):
    template_name = "sem3app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Python'
        context['number'] = 'трех'
        return context


def games(throws, size, message) -> dict:
    return {'results': [f'{message} - {random.randint(*size)}' for _ in range(throws)]}


def head_tails(request, throws):
    context = games(throws, (0, 1), 'На монетке')
    context.update({'title': 'Орел-Решка'})
    return render(request, "sem3app/games.html", context)


def dice(request, throws):
    context = games(throws, (1, 6), 'Вам выпало')
    context.update({'title': 'Кости'})
    return render(request, "sem3app/games.html", context)


def rand100(request, throws):
    context = games(throws, (0, 100), 'Случайное число')
    context.update({'title': 'Случайное число от 0 до 100'})
    return render(request, "sem3app/games.html", context)
