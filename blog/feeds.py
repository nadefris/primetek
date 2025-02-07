from django import forms
from .models import post

class ProductForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'body', 'created_on']

