from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Product
        fields = ['name', 'created_at', 'updated_at', 'price', 'image', 'category']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than or equal to 0.")
        return value

    

    def create(self, validated_data):
        validated_data['name'] = validated_data['name'].lower()
        return super().create(validated_data)