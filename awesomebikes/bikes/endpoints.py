from rest_framework.generics import ListCreateAPIView
from bikes.serializers import BikeSerializer
from bikes.models import Bike


class BikeListView(ListCreateAPIView):
    serializer_class = BikeSerializer

    def get_queryset(self):
        return Bike.objects.all()
