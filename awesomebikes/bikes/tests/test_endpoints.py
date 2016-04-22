from django.core.urlresolvers import resolve
from rest_framework.test import APITestCase
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

    def test_bike_list_uses_bike_serializer(self):
        self.assertEqual(self.view_class().get_serializer_class(), BikeSerializer)
