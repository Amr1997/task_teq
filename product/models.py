from django.db import models
from category.models import Category

class Product(models.Model):
    name = models.JSONField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return str(self.name)