from rest_framework.test import APITestCase
from bikes.models import Bike
from bikes.serializers import BikeSerializer


class BikeSerializerTests(APITestCase):

    def setUp(self):
        self.bike_attributes = {
            'model_name': 'Caloi',
            'size': '52.0'}

        self.bike = Bike.objects.create(**self.bike_attributes)
        self.serializer = BikeSerializer(instance=self.bike)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data

        self.assertIn('model_name', data)
        # self.assertEqual(set(data.keys()), set(['model_name']))

    def test_serializer_model_name_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['model_name'], self.bike_attributes['model_name'])

    def test_serializer_size_field_content(self):
        field = 'size'
        data = self.serializer.data

        self.assertIsInstance(data['size'], float)

