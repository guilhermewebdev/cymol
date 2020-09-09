from django.contrib import admin
from api.admin import cymol, register
from . import models

@register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass
