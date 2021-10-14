from django.contrib import admin
from .models import CookieStand


@admin.register(CookieStand)
class AdminForRecipe(admin.ModelAdmin):
    list_display = ("location", "owner", "created_at")