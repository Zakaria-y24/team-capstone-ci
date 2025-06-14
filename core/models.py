from django.db import models

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