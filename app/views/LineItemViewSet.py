from rest_framework import viewsets
from app.models import Order, LineItem, Catalog, Product
from app.serializers import OrderSerializer, LineItemSerializer, CatalogSerializer, ProductSerializer
from rest_framework.response import Response

class LineItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows list items to be viewed or edited.
    """
    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer
