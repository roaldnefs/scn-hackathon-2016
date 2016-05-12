from django.shortcuts import HttpResponse, render, get_object_or_404
from models import Product, Company


def index(request):
    return render(request, 'index.html', {})


def pricewatch(request):
    return render(request, 'pricewatch.html', {})


def companies(request):
    return render(request, 'companies.html', {})


def company(request, id=None):
    company = get_object_or_404(Company, pk=id)
    return render(
        request,
        'company.html',
        {'company': company}
    )


def product(request, id=None):
    product = get_object_or_404(Product, pk=id)
    return render(
        request,
        'product.html',
        {'product': product})


def about(request):
    return render(request, 'about.html', {})
