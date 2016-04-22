from rest_framework.generics import ListAPIView
from bikes.serializers import BikeSerializer


class BikeListView(ListAPIView):
	serializer_class = BikeSerializer
