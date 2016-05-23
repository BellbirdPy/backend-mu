from rest_framework import viewsets, filters
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_fields = ('establecimiento','estado','lote','categoria','raza','carimbo','estado_sanitario')
    ordering_fields = '__all__'
    ordering = ('caravana',)

