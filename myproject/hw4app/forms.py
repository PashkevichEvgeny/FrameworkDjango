from django import forms

from hw3app.models import Product as Product3
from hw4app.models import Product


class UpdateProductForm(forms.ModelForm):

    class Meta:
        model = Product3
        fields = '__all__'
        initial = 'class'


class UpdateProductAddImageForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['image']
        initial = 'class'

    image = forms.ImageField()


class ImageForm(forms.Form):
    image = forms.ImageField()
