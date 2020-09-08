from django.contrib import admin
from . import models
from api.admin import register, cymol

@register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    pass