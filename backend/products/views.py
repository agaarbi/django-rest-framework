from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetialAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetialAPIView.as_view()