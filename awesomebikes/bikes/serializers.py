from rest_framework import serializers
from bikes.models import Bike

class BikeSerializer(serializers.ModelSerializer):
    size = serializers.FloatField()

    class Meta:
        model = Bike
        fields = ['color', 'size']
