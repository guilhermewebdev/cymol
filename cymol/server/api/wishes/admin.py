from django.contrib import admin
from api.admin import register, cymol
from . import models

@register(models.Wish)
class WishAdmin(admin.ModelAdmin):
    pass
