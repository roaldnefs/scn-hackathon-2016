from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pricewatch$', views.pricewatch, name='pricewatch'),

    url(r'^companies$', views.companies, name='companies'),

    url(r'^product/(?P<slug>[a-zA-Z0-9_.-]+)$', views.product, name='product'),

    url(r'^login$', views.loginview, name='login'),
    url(r'^register$', views.register, name='register'),

    url(r'^dashboard/profile$', views.profile, name='profile'),
    url(r'^dashboard/companies$', views.my_companies, name='my_companies'),
    url(r'^dashboard/products$', views.my_products, name='my_products'),
    url(r'^dashboard/product/(?P<slug>[a-zA-Z0-9_.-]+)$', views.my_product, name='my_product'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),

    url(r'^pay/(?P<reference>[A-Z0-9]+)/(?P<days>\d+)$', views.payment_api, name='payment_api'),

    url(r'^about$', views.about, name='about'),
    url(r'^', views.index, name='index'),
]
