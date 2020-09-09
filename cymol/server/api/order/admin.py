from django.contrib import admin
from api.admin import cymol, register
from . import models

class ProductsInline(admin.TabularInline):
    model = models.ProductToOrder
    extra = 1

@register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductsInline]
