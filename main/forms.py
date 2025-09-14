from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'thumbnail', 'category', 'is_featured', 'sold', 'stock']
        # fields = '__all__'  # untuk memasukkan semua field yang ada di model Product
        # exclude = ['field_yang_tidak_ingin_dimasukkan']  # untuk mengecualikan field tertentu