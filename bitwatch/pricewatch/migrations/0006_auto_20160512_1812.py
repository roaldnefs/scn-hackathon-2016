# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricewatch', '0005_auto_20160512_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='registration_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update_date',
            new_name='modified',
        ),
    ]