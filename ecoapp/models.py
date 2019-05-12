from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.utils.text import slugify
from transliterate import translit
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import os


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])

    def __str__(self):
        return self.name


# Модель продукта
class Product(models.Model):
    title =models.CharField(verbose_name='Заголовок страницы', blank=True, max_length=70)
    keywords = models.CharField(verbose_name='Ключевые слова', blank=True, max_length=255)
    description_seo = models.CharField(verbose_name='Описание страницы', blank=True, max_length=255)
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

    def __str__(self):
        return self.name


class RentaCar(models.Model):
    fio_renta = models.CharField(max_length=255, verbose_name='ФИО')
    phone_renta = models.CharField(max_length=20, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Просмотрено")

    class Meta:
        verbose_name = 'Аренда автомобиля'
        verbose_name_plural = 'Аренда автомобилей'

    def __str__(self):
        return self.fio_renta


class OrderBeton(models.Model):
    fio_beton = models.CharField(max_length=255, verbose_name='ФИО')
    phone_beton = models.CharField(max_length=20, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Просмотрено")

    class Meta:
        verbose_name = 'Заказ бетона'
        verbose_name_plural = 'Заказ бетона'

    def __str__(self):
        return self.fio_beton


def images_folder(instance, filename):
    filename = 'Персональный заказ на имя' + '.' + instance.fio_personal + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.fio_personal, filename)


class PersonalOrder(models.Model):
    fio_personal = models.CharField(max_length=255, verbose_name='ФИО')
    phone_personal = models.CharField(max_length=20, verbose_name='Номер телефона')
    image = models.ImageField(upload_to=images_folder, blank=True, verbose_name="Эскиз проекта")
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Просмотрено")

    class Meta:
        verbose_name = 'Персональный заказ'
        verbose_name_plural = 'Персональные заказы'

    def __str__(self):
        return self.fio_personal


class ProductsWholesale(models.Model):
    fio_wholesales = models.CharField(max_length=255, verbose_name='ФИО')
    phone_wholesales = models.CharField(max_length=20, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Просмотрено")

    class Meta:
        verbose_name = 'Продажа оптом'
        verbose_name_plural = 'Продажа оптом'


class Excursion(models.Model):
    name_university = models.CharField(max_length=255, verbose_name="Название учебного заведения")
    fio_excursion = models.CharField(max_length=255, verbose_name='ФИО преподавателя')
    number_students = models.CharField(max_length=255, verbose_name='Кол-во учащихся')
    phone_excursion = models.CharField(max_length=20, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Просмотрено")

    class Meta:
        verbose_name = 'Запись на экскурсию'
        verbose_name_plural = 'Запись на экскурсию'


class Contacts(models.Model):
    fio_contacts = models.CharField(max_length=255, verbose_name='ФИО')
    phone_contacts = models.CharField(max_length=255, verbose_name='Номер телефона')
    questions_contacts = models.TextField(max_length=500, verbose_name='Вопрос')
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Обработано")

    class Meta:
        verbose_name = 'Вопрос от клиента'
        verbose_name_plural = 'Вопросы от клиентов'


class Comments(models.Model):
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.CharField(max_length=200, verbose_name='Email')
    comment = models.TextField(max_length=500, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = 'Отзыв от клиента'
        verbose_name_plural = 'Отзывы от клиентов'


class Feedbacks(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    phone = models.CharField(max_length=150, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    scaned = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = 'Просьба перезвонить'
        verbose_name_plural = 'Просьба перезвонить'


def avatar_upload_to(instance, filename):
    return os.path.join('uploads', instance.user.username + os.path.splitext(filename)[1])


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, null=True, blank=True)
    phone = models.CharField(max_length=20)
