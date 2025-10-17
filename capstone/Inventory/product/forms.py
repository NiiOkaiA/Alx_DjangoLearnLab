from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Form
        fields=['Product_name','Cost_price','Selling_price','procuct_description','Quantity']
