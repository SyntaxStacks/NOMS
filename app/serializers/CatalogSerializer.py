from rest_framework import serializers
from app.models import Order, LineItem, Catalog, Product

class CatalogSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Catalog
        fields = ('id', 'created', 'name', 'products')
