from django.urls import path
from .views import client_orders, index, client_products_list

urlpatterns = [
    path('', index, name='index'),
    path('client/<int:client_id>/products_list/<int:interval>', client_products_list, name='client_products_list'),
    path('client/<int:client_id>/', client_orders, name='client_orders'),
]