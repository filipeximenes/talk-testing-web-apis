from rest_framework.generics import ListAPIView
from bikes.serializers import BikeSerializer
from bikes.models import Bike


class BikeListView(ListAPIView):
    serializer_class = BikeSerializer

    def get_queryset(self):
        return Bike.objects.all()
