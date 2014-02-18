from rest_framework import serializers
from app.models import Order, LineItem, Catalog, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'created', 'name', 'quantity')
