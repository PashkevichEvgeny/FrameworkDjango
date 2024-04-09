from django.urls import path

from hw4app.views import update_product_form

urlpatterns = [
    path('edit-product/<int:product_id>/', update_product_form, name='update_product_form'),
]
