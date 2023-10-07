from django.urls import path
from product.views import daily_updated_products  , ProductList

urlpatterns = [
    
    path('', ProductList.as_view()),

    path('daily-updated-products/', daily_updated_products),
]
