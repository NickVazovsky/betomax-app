# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-08 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0008_feedbacks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Отзыв от клиента', 'verbose_name_plural': 'Отзывы от клиентов'},
        ),
        migrations.AlterModelOptions(
            name='feedbacks',
            options={'verbose_name': 'Просьба перезвонить', 'verbose_name_plural': 'Просьба перезвонить'},
        ),
    ]
