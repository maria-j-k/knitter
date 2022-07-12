from rest_framework import viewsets

from skeins.models import Colour, Fibre, Manufacturer, Skein
from skeins.serializers import ColourSerializer, FibreSerializer, ManufacturerSerializer, SkeinSerializer


class ManufacturerViewset(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ColourViewset(viewsets.ModelViewSet):
    queryset = Colour.objects.all()
    serializer_class = ColourSerializer


class FibreViewset(viewsets.ModelViewSet):
    queryset = Fibre.objects.all()
    serializer_class = FibreSerializer


class SkeinViewset(viewsets.ModelViewSet):
    queryset = Skein.objects.all()
    serializer_class = SkeinSerializer