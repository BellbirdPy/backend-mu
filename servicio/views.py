import django_filters
from rest_framework import viewsets, filters
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.
class ServicioFilter(filters.FilterSet):
    fecha_15 = django_filters.DateFilter(name="fecha_fin", lookup_expr='lte')
    fecha_hoy = django_filters.DateFilter(name="fecha_fin", lookup_expr='gte')
    class Meta:
        model = Servicio
        fields = ['establecimiento', 'fecha_hoy', 'fecha_15']

class ServicioViewSet(viewsets.ModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_class = ServicioFilter
    ordering_fields = '__all__'
    ordering = ('-fecha_inicio',)

    def create(self, request, *args, **kwargs):
        return super(ServicioViewSet, self).create(request,*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ServicioViewSet, self).destroy(request,*args,**kwargs)
