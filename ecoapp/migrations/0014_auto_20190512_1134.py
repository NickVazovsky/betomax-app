# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-12 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0013_auto_20190510_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_seo',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание страницы'),
        ),
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=70, verbose_name='Заголовок страницы'),
        ),
    ]
