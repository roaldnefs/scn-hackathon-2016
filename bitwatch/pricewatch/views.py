from django.shortcuts import HttpResponse, render, get_object_or_404
from models import Product, Company, Category
from django.core import serializers
from django.utils.safestring import SafeString
from django.db.models import F
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


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
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies': companies})


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


def loginview(request):
    logout(request)
    state = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('dashboard')
            else:
                state = 'Sorry, uw account is nog niet geactiveerd!'
        else:
            state = 'Sorry, uw inlog poging is niet geldig!'
    return render(request, 'login.html', {'state': state})


def register(request):
    return render(request, 'register.html', {})

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html', {})
