from django.db import models
from app.models import Product

class Catalog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    products = models.ManyToManyField(Product)
    
    class Meta:
        ordering = ('created',)
        app_label = 'app'
