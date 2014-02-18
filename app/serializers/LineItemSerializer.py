from rest_framework import serializers
from app.models import Order, LineItem, Catalog, Product


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ('id', 'product', 'created', 'name', 'quantity', 'value')
