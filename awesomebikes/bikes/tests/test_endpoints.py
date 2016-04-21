from django.core.urlresolvers import resolve
from rest_framework.test import APITestCase
from bikes.endpoints import BikeListView


class BikeListTest(APITestCase):

    def test_bike_list_url(self):
        resolver = resolve('/api/bikes/')
        self.assertEqual(resolver.func.__name__, BikeListView.__name__)
