import logging
import random

from django.shortcuts import render

from sem3app.views import head_tails, dice, rand100
from .forms import UserForm, GameForm

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'sem4app/user_form.html', {'form': form})


def game_form(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            name_game = form.cleaned_data['name_game']
            throws = form.cleaned_data['throws']
            match name_game:
                case 'H':
                    return head_tails(request, throws)
                case 'D':
                    return dice(request, throws)
                case 'R':
                    return rand100(request, throws)
            logger.info(f'Получили {name_game=}, {throws=}')
    else:
        form = GameForm()
    return render(request, 'sem4app/game_form.html', {'form': form})
