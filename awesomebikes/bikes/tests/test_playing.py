from rest_framework.test import APITestCase
from bikes.models import Bike
from bikes.serializers import BikeSerializer


class BikeSerializerTests(APITestCase):

    def setUp(self):
        self.bike_attributes = {
            'color': 'Yellow',
            'size': 52.0}

        self.bike = Bike.objects.create(**self.bike_attributes)
        self.serializer = BikeSerializer(instance=self.bike)

    def test_float(self):

        bike = Bike.objects.filter().first()

        s = BikeSerializer(instance=bike, data={'size': 40})

        s.is_valid()
        s.save()

        bike = Bike.objects.filter().first()

        # self.false()

