from rest_framework import viewsets
from app.models import Order, LineItem, Catalog, Product
from app.serializers import OrderSerializer, LineItemSerializer, CatalogSerializer, ProductSerializer
from rest_framework.response import Response

class CatalogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows catalogues to be viewed or edited.
    """
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
