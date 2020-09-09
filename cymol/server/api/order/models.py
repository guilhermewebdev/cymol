from django.db import models
from django.contrib.auth import get_user_model

class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name='orders',
    )
    products = models.ManyToManyField(
        'product.Product',
        related_name='orders'
    )
    registration_date = models.DateTimeField(
        auto_now=True,
    )