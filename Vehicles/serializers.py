from rest_framework import serializers
from .models import VehiclePermit

class VehiclePermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePermit
        fields = '__all__'  # Include all fields from the model


