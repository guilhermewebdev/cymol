from django.db import models
from django.contrib.auth import get_user_model

class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name='orders',
    )
    registration_date = models.DateTimeField(
        auto_now=True,
    )

class ProductToOrder(models.Model):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.DO_NOTHING,
        related_name='orders',
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='products',
    )
    amount = models.IntegerField(
        default=1
    )