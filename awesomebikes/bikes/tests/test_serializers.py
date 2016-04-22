from rest_framework.test import APITestCase
from bikes.models import Bike
from bikes.serializers import BikeSerializer


class BikeSerializerTests(APITestCase):

    def setUp(self):
        self.bike_attributes = {
            'color': 'Yellow',
            'size': '52.0'}

        self.bike = Bike.objects.create(**self.bike_attributes)
        self.serializer = BikeSerializer(instance=self.bike)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['color', 'size']))

    def test_serializer_model_name_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['color'], self.bike_attributes['color'])

    def test_serializer_size_field_content(self):
        data = self.serializer.data

        self.assertIsInstance(data['size'], float)

