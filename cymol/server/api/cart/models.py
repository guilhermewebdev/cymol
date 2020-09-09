from django.db import models
from django.contrib.auth import get_user_model

class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='cart'
    )

class ProductInCart(models.Model):
    product = models.ForeignKey(
        'product.Product',
        related_name='carts',
        on_delete=models.CASCADE,
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='products',
    )