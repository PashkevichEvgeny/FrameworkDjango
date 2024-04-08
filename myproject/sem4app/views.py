import logging

from django.shortcuts import render
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

            logger.info(f'Получили {name_game=}, {throws=}')
    else:
        form = GameForm()
    return render(request, 'sem4app/game_form.html', {'form': form})



