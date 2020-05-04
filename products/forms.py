from django.forms import ModelForm
from .models import Products

class ProductForm (ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'cost_price', 'sale_price', 'icms', 'tax_substitution', 'cst_nfe', 'ncm_nfe', 'unit', 'brand', 'category', 'origin', 'bar_code', 'quantity', 'picture']