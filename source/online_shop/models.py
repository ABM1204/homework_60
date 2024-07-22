from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name', unique=True, null=False)
    description = models.TextField(max_length=200, verbose_name='Category description', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(null=False, max_length=100, verbose_name='Product name')
    description = models.TextField(max_length=200, verbose_name='Product description', blank=True, null=True)
    category = models.ForeignKey('online_shop.Category', on_delete=models.CASCADE, verbose_name='Category', related_name='products')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Add time')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    image = models.URLField(verbose_name='Image URL')
    remainder = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='remainder', default=0)

    def __str__(self):
        return f"name: {self.name}, description: {self.description}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
