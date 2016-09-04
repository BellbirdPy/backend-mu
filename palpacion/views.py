import django_filters
from rest_framework import viewsets, filters
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.

class PalpacionFilter(filters.FilterSet):
    cantidad_actual = django_filters.NumberFilter(name="animalesprenados",lookup_expr='lt')

    class Meta:
        model = Palpacion
        fields = ['establecimiento', 'cantidad_actual']

class PalpacionViewSet(viewsets.ModelViewSet):
    serializer_class = PalpacionSerializer
    queryset = Palpacion.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_class = PalpacionFilter
    ordering_fields = '__all__'
    ordering = ('-fecha',)

class PalpacionDetalleViewSet(viewsets.ModelViewSet):
    serializer_class = DetallesPalpacionSerializer
    queryset = DetallePalpacion.objects.all()