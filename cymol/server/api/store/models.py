from django.db import models
from django.contrib.auth import get_user_model

class Store(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='stores',
    )
    name = models.CharField(
        max_length=100,
    )