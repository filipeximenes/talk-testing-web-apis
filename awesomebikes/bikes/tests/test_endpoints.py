from django.core.urlresolvers import resolve, reverse
from rest_framework.test import APITestCase
from rest_framework import status
from bikes.models import Bike
from bikes.endpoints import BikeListView
from bikes.serializers import BikeSerializer


class BikeListTest(APITestCase):
    view_class = BikeListView
    view = view_class.as_view()
    view_name = 'bikes-list'

    def setUp(self):
        self.bike_data = {
            'color': 'yellow',
            'size': '52.00'
        }

    def test_bike_list_url(self):
        resolver = resolve('/api/bikes/')
        self.assertEqual(resolver.func.__name__, self.view_class.__name__)

    def test_bike_list_url_name(self):
        resolver = resolve('/api/bikes/')
        self.assertEqual(resolver.url_name, self.view_name)

    def test_bike_list_returns_200(self):
        response = self.client.get(reverse(self.view_name))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bike_list_returns_a_list(self):
        response = self.client.get(reverse(self.view_name))

        self.assertIsInstance(response.data, list)

    def test_bike_list_uses_bike_serializer(self):
        self.assertEqual(self.view_class().get_serializer_class(), BikeSerializer)

    def test_create_bike_returns_201(self):
        response = self.client.post(reverse(self.view_name), self.bike_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_bike_correctly_saves_to_db(self):
        self.client.post(reverse(self.view_name), self.bike_data)

        bikes = Bike.objects.all()

        self.assertEqual(len(bikes), 1)

        bike = bikes[0]

        self.assertEqual(bike.color, self.bike_data['color'])
        self.assertEqual(str(bike.size), self.bike_data['size'])

    # def test_returns_400_on_errors(self):
    #     self.bike_data = {
    #         'color': 'wrong color value',
    #         'size': '52.00',
    #     }

    #     response = self.client.post(reverse(self.view_name), self.bike_data)

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(set(response.errors.keys()))
