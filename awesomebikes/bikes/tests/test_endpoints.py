from django.core.urlresolvers import resolve
from rest_framework.test import APITestCase
from bikes.endpoints import BikeListView


class BikeListTest(APITestCase):
    view = BikeListView
    view_name = 'bikes-list'

    def test_bike_list_url(self):
        resolver = resolve('/api/bikes/')
        self.assertEqual(resolver.func.__name__, self.view.__name__)

    def test_bike_list_url_name(self):
        resolver = resolve('/api/bikes/')
        self.assertEqual(resolver.url_name, self.view_name)
