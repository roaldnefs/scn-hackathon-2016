# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricewatch', '0011_auto_20160513_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
