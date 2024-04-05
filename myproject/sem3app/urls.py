from django.urls import path
from . import views
from .views import TemplateAbout

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/', TemplateAbout.as_view(), name='about'),
]