from django import forms
from django.forms import TextInput

from hw3app.models import Product


class UpdateProductForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['name'].initial = self.instance.name

    name = forms.CharField(initial='class', max_length=100)
    description = forms.CharField(initial='class', max_length=1000)
    price = forms.DecimalField(initial='class', max_digits=8, decimal_places=2)
    amount = forms.IntegerField(initial='class')

    class Meta:
        model = Product
        fields = '__all__'

