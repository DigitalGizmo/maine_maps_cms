from rest_framework import generics
from .models import MapSet
from .serializers import MapSetSerializer


class MapSetList(generics.ListAPIView):
    queryset = MapSet.objects.prefetch_related('views')
    serializer_class = MapSetSerializer


class MapSetDetail(generics.RetrieveAPIView):
    queryset = MapSet.objects.prefetch_related('views')
    serializer_class = MapSetSerializer
    lookup_field = 'slug'
