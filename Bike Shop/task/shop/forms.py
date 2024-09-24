from django import forms
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number']
        labels = {
            'name': 'your name',
            'surname': 'your surname',
            'phone_number': 'your phone number',
        }
        widgets = {
            'name': forms.TextInput(attrs={'max_length': 255, 'required': True}),
            'surname': forms.TextInput(attrs={'max_length': 255, 'required': True}),
            'phone_number': forms.TextInput(attrs={'max_length': 255, 'required': True}),
        }
