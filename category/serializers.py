from rest_framework import serializers
from .models import Category 

class CategorySerializer(serializers.ModelSerializer):
    total_products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'total_products']

    def get_total_products(self, category):
        return category.product_set.count()
