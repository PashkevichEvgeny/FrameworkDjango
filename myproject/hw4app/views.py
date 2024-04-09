from django.shortcuts import render, redirect

from hw3app.models import Product
from hw4app.forms import UpdateProductForm
import logging

# Create your views here.

logger = logging.getLogger(__name__)


def update_product_form(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    if request.method == 'POST':
        form = UpdateProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            logger.info(f'Получили {form.cleaned_data=}')
            return redirect('update_product_form', product_id)
    else:
        # Заполнение плейсхолдеров предыдущими значениями продукта
        form = UpdateProductForm(initial={'name': product.name,
                                          'description': product.description,
                                          'price': product.price,
                                          'amount': product.amount})
    return render(request, 'hw4app/form.html', {'form': form})
