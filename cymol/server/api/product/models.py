from django.db import models

class Product(models.Model):
    price = models.FloatField(
        verbose_name='price',
        null=True,
    )
    name = models.CharField(
        max_length=100,
    )
    description = models.CharField(
        max_length=1000,
    )
    stock = models.IntegerField(
        verbose_name='stock amount',
        default=1,
    )

class ProductImage(models.Model):
    image = models.ImageField(
        verbose_name='image',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )