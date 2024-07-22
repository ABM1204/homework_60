from django.contrib import admin

from online_shop.models import Product, Category, Order

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'image', 'reminder')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone', 'address', 'created_at')
