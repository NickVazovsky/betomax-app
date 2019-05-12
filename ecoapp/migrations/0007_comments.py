# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-08 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0006_auto_20190508_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('comment', models.TextField(max_length=500, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scaned', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecoapp.Product')),
            ],
        ),
    ]