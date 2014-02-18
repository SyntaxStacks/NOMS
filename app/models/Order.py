from django.db import models
from app.models import LineItem

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    vendor = models.TextField()
    customer = models.TextField()
    lineItems = models.ManyToManyField(LineItem)

    class Meta:
        ordering = ('created',)
        app_label = 'app'
