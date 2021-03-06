from django.shortcuts import HttpResponse, render, get_object_or_404
from models import Product, Company, Category, Advertisement
from forms import CompanyForm, ProductForm, UserForm, ProfileForm
from django.core import serializers
from django.utils.safestring import SafeString
from django.db.models import F
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import _get_queryset

import json
import requests
from datetime import datetime, timedelta
import urllib


def get_rate_of_exchange():
    url = 'http://bitcoinkopen.com/api/daycourses.json'
    request = requests.get(url)
    data = json.loads(request.text)[0]
    return data['EUR']['24h']


def get_object_or_none(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None


def index(request):
    return render(request, 'index.html', {})


def pricewatch(request):
    exchange_rate = get_rate_of_exchange()
    products_json = serializers.serialize('json', Product.objects.all())
    companies = Company.objects.all()
    categories = Category.objects.all()
    advertisements = [ad.product.id for ad in Advertisement.objects.filter(start__lte=timezone.now(), end__gte=timezone.now())]
    advertisements_json = json.dumps(advertisements)

    return render(
        request,
        'pricewatch.html',
        {'products_json': SafeString(products_json), 'advertisements_json': SafeString(advertisements_json), 'companies': companies, 'categories': categories, 'exchange_rate': exchange_rate})


def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies': companies})


def product(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    # Do a transaction to increment the views.
    Product.objects.filter(pk=product.id).update(views=F('views') + 1)
    if request.method == 'POST':
        phonenumber = request.POST['phonenumber']
        message = 'Hi, ' + product.name + ' (' + product.url + ')'
        url = 'http://0.0.0.0:5000/sms?to=' + urllib.quote_plus(str(phonenumber)) + '&message=' + urllib.quote_plus(str(message))
        print('URL: ' + url)
        r = requests.get(url)
        print(r.status_code)

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
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return HttpResponseRedirect('login')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required(login_url='login')
def dashboard(request):
    part = Product.objects.all().order_by('views').reverse()[:5]
    products = Product.objects.all()
    return render(request, 'dashboard.html', {'part':part, 'product':product})


@login_required(login_url='login')
def profile(request):
    user = request.user
    password_error_state = None
    password_success_state = None
    if request.POST:
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        check_password = request.POST['check_password']
        if new_password == check_password:
            if authenticate(username=user.username, password=old_password):
                user.set_password(new_password)
                user.save()
                password_success_state = 'Wachtwoord succesvol gewijzigd!'
            else:
                password_error_state = 'Huidige wachtwoord onjuist!'
        else:
            password_error_state = 'Nieuwe wachtwoord komt niet overeen met de wachtwoord check!'

    return render(request, 'profile.html', {'password_error_state': password_error_state, 'password_success_state': password_success_state})


@login_required(login_url='login')
def my_companies(request):
    user = request.user
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = user
            form.save()
    else:
        form = CompanyForm()
    companies = Company.objects.filter(owner=user)
    return render(request, 'my_companies.html', {'companies': companies, 'form': form})


@login_required(login_url='login')
def my_products(request):
    user = request.user
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    companies = Company.objects.filter(owner=user)
    products = Product.objects.filter(company__in=companies)
    exchange_rate = get_rate_of_exchange()
    return render(request, 'my_products.html', {'products': products, 'form': form, 'exchange_rate': exchange_rate})


@login_required(login_url='login')
def my_product(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            updated_product = form.save(commit=False)
            updated_product.id = product.id
            updated_product.created = product.created
            updated_product.save()
    else:
        form = ProductForm(instance=product)
    return render(request, 'my_product.html', {'form': form, 'product': product})

@login_required(login_url='login')
def my_company(request, id=None):
    company = get_object_or_404(Company, pk=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            updated_company = form.save(commit=False)
            updated_company.id = company.id
            updated_company.owner = company.owner
            updated_company.save()
    else:
        form = CompanyForm(instance=company)
    return render(request, 'my_company.html', {'form': form, 'company': company})


@login_required(login_url='login')
def my_advertisement(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    advertisement = get_object_or_none(Advertisement, product=product)
    if advertisement is None:
        advertisement = Advertisement()
        advertisement.product = product
        advertisement.save()
    return render(request, 'my_advertisement.html', {'advertisement': advertisement, 'product': product})


def payment_api(request, reference=None, days=None):
    if reference is not None and days is not None:
        advertisement = Advertisement.objects.get(reference=reference)
        if advertisement is not None:
            if advertisement.end is None or advertisement.end < timezone.now():
                advertisement.start = timezone.now()
                advertisement.end = timezone.now() + timedelta(days=int(days))
            elif advertisement.start < timezone.now() and advertisement.end > timezone.now():
                advertisement.end += timedelta(days=int(days))
            advertisement.save()
            return HttpResponse('OK')
    return HttpResponse('FAIL')
