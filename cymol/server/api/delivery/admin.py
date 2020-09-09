from django.contrib import admin
from api.admin import cymol, register
from . import models

class ProductsInline(admin.TabularInline):
    extra = 1
    model = models.ProductToDelivery

@register(models.Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    inlines = [ProductsInline]