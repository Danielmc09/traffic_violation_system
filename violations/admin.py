from django.contrib import admin
from .models import Violation


@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'officer', 'timestamp', 'comments', 'created_at', 'updated_at')
    search_fields = ('vehicle__license_plate', 'officer__user__username', 'comments')
    list_filter = ('timestamp', 'vehicle__license_plate', 'officer__user__username')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(officer__user=request.user)
