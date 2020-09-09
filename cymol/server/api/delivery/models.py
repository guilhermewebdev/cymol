from django.db import models
from django.contrib.auth import get_user_model

class Delivery(models.Model):
    deliverer = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name='deliveries',
    )
    order = models.ForeignKey(
        'order.Order',
        on_delete=models.DO_NOTHING,
        related_name='deliveries',
    )
    price = models.FloatField(
        verbose_name='price',
    )

class ProductToDelivery(models.Model):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.DO_NOTHING,
        related_name='deliveries',
    )
    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        related_name='products',
    )