# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-08 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ecoapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_university', models.CharField(max_length=255, verbose_name='Название учебного заведения')),
                ('fio_excursion', models.CharField(max_length=255, verbose_name='ФИО преподавателя')),
                ('number_students', models.CharField(max_length=255, verbose_name='Кол-во учащихся')),
                ('phone_excursion', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scaned', models.BooleanField(default=True, verbose_name='Просмотрено')),
            ],
            options={
                'verbose_name': 'Запись на экскурсию',
                'verbose_name_plural': 'Запись на экскурсию',
            },
        ),
        migrations.CreateModel(
            name='OrderBeton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_beton', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone_beton', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scaned', models.BooleanField(default=True, verbose_name='Просмотрено')),
            ],
            options={
                'verbose_name': 'Заказ бетона',
                'verbose_name_plural': 'Заказ бетона',
            },
        ),
        migrations.CreateModel(
            name='PersonalOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_personal', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone_personal', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('image', models.ImageField(blank=True, upload_to=ecoapp.models.images_folder, verbose_name='Эскиз проекта')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scaned', models.BooleanField(default=True, verbose_name='Просмотрено')),
            ],
            options={
                'verbose_name': 'Персональный заказ',
                'verbose_name_plural': 'Персональные заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(verbose_name='На складе')),
                ('available', models.BooleanField(default=True, verbose_name='Доступен')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecoapp.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductsWholesale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_wholesales', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone_wholesales', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scaned', models.BooleanField(default=True, verbose_name='Просмотрено')),
            ],
            options={
                'verbose_name': 'Продажа оптом',
                'verbose_name_plural': 'Продажа оптом',
            },
        ),
        migrations.CreateModel(
            name='RentaCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_renta', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone_renta', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scaned', models.BooleanField(default=True, verbose_name='Просмотрено')),
            ],
            options={
                'verbose_name': 'Аренда автомобиля',
                'verbose_name_plural': 'Аренда автомобилей',
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]