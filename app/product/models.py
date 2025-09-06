from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    def __str__(self):
        return str(self.name)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()

class Order(models.Model):
    items = models.ManyToManyField(OrderItem, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='orders')

class Cart(models.Model):
    class CartStatus(models.TextChoices):
        PENDING = "pending"
        PAID = "paid"
    items = models.ManyToManyField(OrderItem, related_name='carts')
    status = models.CharField(max_length=255, choices=CartStatus.choices, default=CartStatus.PENDING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='carts')