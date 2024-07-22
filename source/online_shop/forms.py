from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image', 'remainder']

    def clean_remainder(self):
        remainder = self.cleaned_data.get('remainder')
        if remainder < 0:
            raise forms.ValidationError("Remainder cannot be less than 0.")
        return remainder



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'phone', 'address']