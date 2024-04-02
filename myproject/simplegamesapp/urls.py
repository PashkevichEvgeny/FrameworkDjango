from django.urls import path
from . import views


urlpatterns = [
    path('head-tails/', views.head_tails, name='head_tails'),
    path('dice/', views.dice, name='dice'),
    path('rand100/', views.rand100, name='rand100')
]