from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product

@receiver(pre_save, sender=Product)
def limit_products_in_category(sender, instance, **kwargs):
    category = instance.category
    if category.product_set.count() >= 5:
        raise ValueError("Can't add more than 5 products to a one category.")