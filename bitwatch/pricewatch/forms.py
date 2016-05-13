from django.forms import ModelForm
from models import Company, Product


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['owner']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'views', 'created', 'modified']
