from rest_framework import viewsets
from app.models import Order, LineItem, Catalog, Product
from app.serializers import OrderSerializer, LineItemSerializer, CatalogSerializer, ProductSerializer
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    #def create(self, request
