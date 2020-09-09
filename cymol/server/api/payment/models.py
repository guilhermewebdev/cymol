from django.db import models
from django.contrib.auth import get_user_model

class Payment(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name='payments',
    )
    order = models.OneToOneField(
        'order.Order',
        on_delete=models.DO_NOTHING,
        related_name='payment',
    )