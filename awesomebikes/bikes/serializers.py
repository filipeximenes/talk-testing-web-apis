from rest_framework import serializers
from bikes.models import Bike

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['model_name']
