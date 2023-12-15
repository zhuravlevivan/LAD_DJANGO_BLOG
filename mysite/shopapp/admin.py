from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price', 'discount')
    list_display_links = ('pk', 'name')


