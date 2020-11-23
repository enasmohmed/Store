from django.forms import ModelForm

from products.models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('brand', 'title', 'description', 'price', 'image', 'sale', 'new')


