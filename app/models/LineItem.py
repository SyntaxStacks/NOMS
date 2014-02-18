from django.db import models
from app.models import Product

class LineItem(models.Model): 
    product = models.ForeignKey(Product)
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField();
    quantity = models.IntegerField()
    value = models.TextField();

    class Meta:
        ordering = ('created',)
        app_label = 'app'
