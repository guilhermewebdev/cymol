from django.contrib import admin
from api.admin import cymol, register
from . import models

@register(models.Payment)
class PaymentsAdmin(admin.ModelAdmin):
    pass