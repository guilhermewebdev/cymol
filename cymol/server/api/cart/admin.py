from django.contrib import admin
from api.admin import register, cymol
from . import models

@register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    pass