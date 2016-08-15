# Create your views here.
from rest_framework import filters
from rest_framework import viewsets

from genetica.models import LoteGenetica, AnimalGenetica
from genetica.serializers import LoteGeneticaSerializer, AnimalGeneticaSerializer


class LoteGeneticaViewSet(viewsets.ModelViewSet):
    serializer_class = LoteGeneticaSerializer
    queryset = LoteGenetica.objects.all()
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('establecimiento',)


class AnimalGeneticaViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalGeneticaSerializer
    queryset = AnimalGenetica.objects.all()
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('establecimiento',)
