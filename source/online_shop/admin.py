from django.contrib import admin

from online_shop.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'image', 'reminder')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
