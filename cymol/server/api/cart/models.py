from django.db import models
from django.contrib.auth import get_user_model

class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='cart'
    )
    products = models.ManyToManyField(
        'product.Product',
        related_name='carts',
    )