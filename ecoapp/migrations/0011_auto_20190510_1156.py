# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-10 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='info',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
