from rest_framework import viewsets
from app.models import Order, LineItem, Catalog, Product
from app.serializers import OrderSerializer, LineItemSerializer, CatalogSerializer, ProductSerializer
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
