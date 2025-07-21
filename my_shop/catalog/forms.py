from django import forms
from .models import Items


class ItemForm(forms.ModelForm):
    class Meta:
        model  = Items
        fields = ["item_name", "price", "category", "in_stock"]   # include them!