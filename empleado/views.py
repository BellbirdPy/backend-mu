from rest_framework import viewsets,filters
from serializers import *
from models import *

# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('apellido',)


class ContratistaViewSet(viewsets.ModelViewSet):
    serializer_class = ContratistaSerializer
    queryset = Contratista.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('apellido',)
