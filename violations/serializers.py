from rest_framework import serializers
from .models import Violation
from vehicles.serializers import VehicleSerializer
from officers.serializers import OfficerSerializer


class ViolationSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    officer = OfficerSerializer()

    class Meta:
        model = Violation
        fields = ['id', 'timestamp', 'comments', 'vehicle', 'officer']
