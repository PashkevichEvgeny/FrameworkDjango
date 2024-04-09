from django.urls import path

from hw4app.views import update_product_form, upload_image, update_product_add_image_form

urlpatterns = [
    path('edit-product/<int:product_id>/', update_product_form, name='update_product_form'),
    path('create-product/<int:product_id>/', update_product_add_image_form, name='update_product_add_image_form'),
    path('upload/', upload_image, name='upload_image'),
]
