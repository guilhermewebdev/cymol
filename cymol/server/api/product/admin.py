from django.contrib import admin
from api.admin import register, cymol
from . import models

class ProductImageAdminInline(admin.TabularInline):
    extra = 1
    model = models.ProductImage

@register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdminInline]