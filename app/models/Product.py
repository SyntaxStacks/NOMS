from django.db import models

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    quantity = models.IntegerField()

    class Meta:
        ordering = ('created',)
        app_label = 'app'
