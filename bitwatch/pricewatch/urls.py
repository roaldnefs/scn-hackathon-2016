from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pricewatch$', views.pricewatch, name='pricewatch'),

    url(r'^companies$', views.companies, name='companies'),
    url(r'^company/(?P<id>[0-9]+)$', views.company, name='company'),

    url(r'^product/(?P<slug>[a-zA-Z0-9_.-]+)$', views.product, name='product'),

    url(r'^about$', views.about, name='about'),
    url(r'^', views.index, name='index'),
]
