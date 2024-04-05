from django.urls import path
from . import views
from .views import TemplateAbout

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/', TemplateAbout.as_view(), name='about'),
    path('head-tails/<int:throws>', views.head_tails, name='head_tails'),
    path('dice/<int:throws>', views.dice, name='dice'),
    path('rand100/<int:throws>', views.rand100, name='rand100')
]