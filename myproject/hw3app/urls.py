from django.urls import path
from .views import client_orders, index

urlpatterns = [
    path('', index, name='index'),
    path('client/<int:client_id>/', client_orders, name='client_orders'),
]