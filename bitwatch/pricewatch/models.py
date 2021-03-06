from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categorieen'

    def __unicode__(self):
        return u'%s' % (self.name)


class Company(models.Model):
    name = models.CharField(max_length=128)
    kvk = models.IntegerField()
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    owner = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name = 'bedrijf'
        verbose_name_plural = 'bedrijven'

    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)
        if not self.id:
            self.id = slugify(self.name + ' ' + str(self.id))
            self.save()

    def __unicode__(self):
        return u'%s (%d)' % (self.name, self.kvk)


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    url = models.URLField()
    image = models.URLField(blank=True)
    views = models.IntegerField(default=0, editable=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category)
    company = models.ForeignKey(Company)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'producten'

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name + ' ' + str(self.id))
            self.save()

    def __unicode__(self):
        return u'%s - %s - %d' % (self.name, self.company.name, self.price)


class Advertisement(models.Model):
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    reference = models.CharField(max_length=255, editable=False, unique=True)
    product = models.ForeignKey(Product)

    class Meta:
        verbose_name = 'advertentie'
        verbose_name_plural = 'advertenties'

    def save(self, *args, **kwargs):
        super(Advertisement, self).save(*args, **kwargs)
        if not self.reference:
            self.reference = str(self.id) + uuid.uuid4().hex[:19].upper()
            self.save()

    def __unicode__(self):
        return u'%s' % (self.product.name)


class Profile(models.Model):
    user = models.OneToOneField(User)
    phonenumber = models.CharField(max_length=13)

    def __unicode__(self):
        return u'%s %s' % (self.user.username, self.phonenumber)
