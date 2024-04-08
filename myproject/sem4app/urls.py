from django.urls import path

from sem4app.views import user_form, game_form, add_author, add_post

urlpatterns = [
    path('form/', user_form, name='user_form'),
    path('game/', game_form, name='game_form'),
    path('add-author/', add_author, name='add_form'),
    path('add-post/', add_post, name='add_post'),
]