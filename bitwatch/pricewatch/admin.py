from django.contrib import admin

from . import models


class CompanyAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Company
        exclude = []


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['views', 'created', 'modified', 'slug']

    class Meta:
        model = models.Product
        exclude = []


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Category
        exclude = []


class AdvertisementAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Advertisement
        exclude = []


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Advertisement, AdvertisementAdmin)
