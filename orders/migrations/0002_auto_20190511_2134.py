# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-11 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='Самовывоз', max_length=250, verbose_name='Адрес'),
        ),
    ]
