from django.contrib import admin
from api.admin import register, cymol
from . import models

class ProductsToCardInline(admin.TabularInline):
    model = models.ProductInCart
    extra = 1

@register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [ProductsToCardInline]