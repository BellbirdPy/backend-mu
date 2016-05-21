from rest_framework import viewsets,filters
from serializers import *
from models import *
# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

class EventoEstablecimientoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoEstablecimientoSerializer
    queryset = EventoEstablecimiento.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('establecimiento',)
