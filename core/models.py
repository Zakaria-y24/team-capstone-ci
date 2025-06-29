from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('flowers', 'Flowers'),
        ('leaves', 'Leaves'),
        ('seasonal', 'Seasonal'),
        ('misc', 'Miscellaneous'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='misc')
    stock = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.user or self.session_key})"

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"