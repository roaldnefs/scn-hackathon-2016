from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'index.html', {})


def pricewatch(request):
    return render(request, 'pricewatch.html', {})


def companies(request):
    return render(request, 'companies.html', {})


def company(request, id=None):
    return render(request, 'company.html', {})


def product(request, id=None):
    return render(request, 'product.html', {})


def about(request):
    return render(request, 'about.html', {})
