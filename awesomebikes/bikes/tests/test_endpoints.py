from django.core.urlresolvers import resolve, reverse
from rest_framework.test import APITestCase
from rest_framework import status
from bikes.endpoints import BikeListView
from bikes.serializers import BikeSerializer


class BikeListTest(APITestCase):
    view_class = BikeListView
    view = view_class.as_view()
    view_name = 'bikes-list'

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
