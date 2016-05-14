from django.forms import ModelForm
from django import forms
from models import Company, Product
from django.contrib.auth.models import User


class CompanyForm(ModelForm):
    class Meta:
        labels = {
            'name': 'Naam',
            'kvk': 'KvK nummer',
            'description': 'Beschrijving',
            'url': 'URL',
        }
        model = Company
        exclude = ['owner']


class ProductForm(ModelForm):

    class Meta:
        labels = {
            'name': 'Naam',
            'description': 'Beschrijving',
            'price': 'Prijs',
            'url': 'URL',
            'image': 'Afbeelding (link naar)',
            'category': 'Cateforie',
            'company': 'Bedrijf'
        }
        model = Product
        exclude = ['slug', 'views', 'created', 'modified']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
