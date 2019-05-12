from django.contrib import admin
from .models import Category, Product, RentaCar, OrderBeton, PersonalOrder, ProductsWholesale, Excursion, Contacts, \
    Comments, Feedbacks, UserProfile

# Register your models here.
admin.site.site_header = 'BETOMAX-ADMIN'


class RentacartAdmin(admin.ModelAdmin):
    list_display = ['fio_renta', 'phone_renta', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class OrderBetonAdmin(admin.ModelAdmin):
    list_display = ['fio_beton', 'phone_beton', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class PersonalOrderAdmin(admin.ModelAdmin):
    list_display = ['fio_personal', 'phone_personal', 'image', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class WhosalesProductAdmin(admin.ModelAdmin):
    list_display = ['fio_wholesales', 'phone_wholesales', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class ExcursionAdmin(admin.ModelAdmin):
    list_display = ['name_university', 'fio_excursion', 'phone_excursion', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['fio_contacts', 'phone_contacts', 'questions_contacts', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'email', 'comment', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created', 'scaned']
    list_filter = ['created', 'scaned']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['phone', 'avatar']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RentaCar, RentacartAdmin)
admin.site.register(OrderBeton, OrderBetonAdmin)
admin.site.register(PersonalOrder, PersonalOrderAdmin)
admin.site.register(ProductsWholesale, WhosalesProductAdmin)
admin.site.register(Excursion, ExcursionAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Feedbacks, FeedbackAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
