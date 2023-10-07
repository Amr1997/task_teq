from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def daily_updated_products(request):
    today = date.today()
    products = Product.objects.filter(updated_at__date=today)
    total_price = sum(product.price for product in products)
    count = len(products)

    data = {
        'products': [
            {'id': product.id, 'price': product.price}
            for product in products
        ],
        'total_price': total_price,
        'count': count
    }
    return Response(data)