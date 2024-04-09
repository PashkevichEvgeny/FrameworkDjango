from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from hw3app.models import Product as Product3
from hw4app.models import Product
from hw4app.forms import UpdateProductForm, ImageForm, UpdateProductAddImageForm
import logging

# Create your views here.

logger = logging.getLogger(__name__)


def update_product_form(request, product_id):
    product = Product3.objects.filter(pk=product_id).first()
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


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    title = 'Загрузить изображение'
    return render(request, 'hw4app/upload_image.html', {'form': form, 'title': title})


def update_product_add_image_form(request, product_id):
    if request.method == 'POST':
        form = UpdateProductAddImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Создание нового продукта или редактирование уже существующего
            updated, created = Product.objects.update_or_create(
                pk=product_id,
                defaults={
                    'name': form.cleaned_data['name'],
                    'description': form.cleaned_data['description'],
                    'price': form.cleaned_data['price'],
                    'amount': form.cleaned_data['amount'],
                    'image': form.cleaned_data['image']})
            # Сохранение изображения
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            logger.info(f'Получили {form.cleaned_data["name"]} {updated=} {created=}')
            return redirect('update_product_add_image_form', product_id)
    else:
        if product := Product.objects.filter(pk=product_id).first():
            # Заполнение плейсхолдеров предыдущими значениями продукта
            form = UpdateProductAddImageForm(initial={'name': product.name,
                                                      'description': product.description,
                                                      'price': product.price,
                                                      'amount': product.amount})
        else:
            # Заполнение плейсхолдеров значениями по умолчанию
            form = UpdateProductAddImageForm(initial={'name': 'New product',
                                                      'description': 'Description',
                                                      'price': 0,
                                                      'amount': 0})
    title = 'Создать новый продукт или изменить существующий'
    return render(request, 'hw4app/upload_image.html', {'form': form, 'title': title})
