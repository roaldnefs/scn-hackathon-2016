from django.forms import ModelForm
from django import forms
from models import Company, Product
from django.contrib.auth.models import User


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['owner']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'views', 'created', 'modified']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
