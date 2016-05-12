from django.shortcuts import HttpResponse, render, get_object_or_404
from models import Product, Company, Category
from django.core import serializers
from django.utils.safestring import SafeString
from django.db.models import F


def index(request):
    return render(request, 'index.html', {})


def pricewatch(request):
    products_json = serializers.serialize('json', Product.objects.all())
    companies = Company.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'pricewatch.html',
        {'products_json': SafeString(products_json), 'companies': companies, 'categories': categories})


def companies(request):
    return render(request, 'companies.html', {})


def company(request, slug=None):
    company = get_object_or_404(Company, pk=id)
    return render(
        request,
        'company.html',
        {'company': company}
    )


def product(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    # Do a transaction to increment the views.
    Product.objects.filter(pk=product.id).update(views=F('views') + 1)
    return render(
        request,
        'product.html',
        {'product': product})


def about(request):
    return render(request, 'about.html', {})
