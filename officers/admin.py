from django.contrib import admin
from .models import Officer

# Register your models here.


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name', 'badge_number', 'user', 'created_at', 'updated_at')
    search_fields = ('name', 'badge_number', 'user__username')
