# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-08 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0003_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Вопрос от клиента', 'verbose_name_plural': 'Вопросы от клиентов'},
        ),
    ]