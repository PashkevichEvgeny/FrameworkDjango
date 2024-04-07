import random

from django.shortcuts import render, get_object_or_404

from hw3app.models import Client, Order


def index(request):
    client = get_object_or_404(Client, pk=random.randint(1, 3))
    return render(request, 'hw3app/index.html', {'client': client})


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client.id)
    return render(request, 'hw3app/client_orders.html', {'client': client, 'orders': orders})
