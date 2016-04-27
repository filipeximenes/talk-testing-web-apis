from rest_framework import serializers
from bikes.models import Bike


class BikeSerializer(serializers.ModelSerializer):
    size = serializers.FloatField(min_value=30.0, max_value=60.0)

    class Meta:
        model = Bike
        fields = ['color', 'size']
