import datetime
import random
from django.shortcuts import render, get_object_or_404
from hw3app.models import Client, Order


def index(request):
    client = get_object_or_404(Client, pk=random.randint(1, 3))
    interval = random.choice((7, 31, 365))
    return render(request, 'hw3app/index.html', {'client': client, 'interval': interval})


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client.id)
    return render(request, 'hw3app/client_orders.html', {'client': client, 'orders': orders})


def client_products_list(request, client_id, interval):
    products = list()
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client.id).order_by('created')

    for order in orders:
        if order.created.timestamp() > (datetime.datetime.now() - datetime.timedelta(days=interval)).timestamp():
            for product in order.products.all():
                if product not in products:
                    products.append(product)
    return render(request, 'hw3app/client_products_list.html', {'client': client,
                                                                'products': products,
                                                                'interval': interval,
                                                                })
