from django.db import models
from django.contrib.auth import get_user_model

class Wish(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='wishes',
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='wishes',
    )
    registration_date = models.DateTimeField(
        verbose_name='registration date',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'wish'
        verbose_name_plural = 'wishes'