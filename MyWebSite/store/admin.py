from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug', 'price', 'stock', 'is_available', 'modified_date', 'category')

admin.site.register(Product, ProductAdmin)