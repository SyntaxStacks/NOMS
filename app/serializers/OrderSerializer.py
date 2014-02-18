from rest_framework import serializers
from app.models import Order, LineItem, Catalog, Product

class OrderSerializer(serializers.ModelSerializer):
    lineItems = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Order
        fields = ('id', 'created', 'vendor', 'customer', 'lineItems')
