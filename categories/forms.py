from django import forms
from .models import Category,SubCategory, Brand

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category

        fields = [
            'name',
            'image'
        ]