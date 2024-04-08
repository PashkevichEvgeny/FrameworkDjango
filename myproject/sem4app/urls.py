from django.urls import path

from sem4app.views import user_form, game_form

urlpatterns = [
    path('form/', user_form, name='user_form'),
    path('game/', game_form, name='game_form'),
]