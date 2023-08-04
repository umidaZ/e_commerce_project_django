from django.contrib import admin
from . models import Product, Category, Cart
# Register your models here.

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image']
    ordering = ('name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
