
from rest_framework import viewsets, filters
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.

class ServicioViewSet(viewsets.ModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('-fecha_inicio',)

    def create(self, request, *args, **kwargs):
        return super(ServicioViewSet, self).create(request,*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ServicioViewSet, self).destroy(request,*args,**kwargs)
