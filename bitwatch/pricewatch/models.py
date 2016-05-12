from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Company(models.Model):
    name = models.CharField(max_length=128)
    # TODO KvK nummer bestaat uit 8 cijfers
    kvk = models.IntegerField()
    description = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return u'%s (%d)' % (self.name, self.kvk)


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=8)
    url = models.URLField(blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return u'%s - %s - %d' % (self.name, self.company.name, self.price)
