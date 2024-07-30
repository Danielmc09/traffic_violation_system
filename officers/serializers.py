from rest_framework import serializers
from .models import Officer


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['name', 'badge_number']
