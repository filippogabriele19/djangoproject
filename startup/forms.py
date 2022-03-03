from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description")


class CodeForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
        )
