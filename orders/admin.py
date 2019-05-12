from django.contrib import admin
from .models import Order, OrderItem
from django.core.urlresolvers import reverse
from django.utils.html import format_html


def OrderPDF(obj):
    return format_html('<a href="{}">PDF</a>'.format(
        reverse('orders:AdminOrderPDF', args=[obj.id])
    ))


OrderPDF.short_description = 'В PDF'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', OrderPDF]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
