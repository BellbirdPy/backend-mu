from rest_framework import viewsets,filters

from scripts.related_ordering import RelatedOrderingFilter
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

class VacunacionViewSet(viewsets.ModelViewSet):
    serializer_class = VacunacionSerializer
    queryset = Vacunacion.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('fecha_vacunacion',)

    def create(self, request, *args, **kwargs):
        return super(VacunacionViewSet, self).create(request,*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            pass
        return super(VacunacionViewSet, self).destroy(request,*args,**kwargs)
