from rest_framework.decorators import api_view
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data) 

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)