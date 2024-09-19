from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializer
from products.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post']
    