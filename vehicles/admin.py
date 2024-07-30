from django.contrib import admin
from .models import Vehicle

# Register your models here.


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'brand', 'color', 'owner', 'created_at', 'updated_at')
    search_fields = ('license_plate', 'brand', 'color', 'owner__name')
    list_filter = ('brand', 'color')
