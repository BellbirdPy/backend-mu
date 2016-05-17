from rest_framework import viewsets, filters
from serializers import *
from models import *

# Create your views here.
class CompraViewSet(viewsets.ModelViewSet):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('establecimiento',)

class DetalleCompraViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleCompraSerialzer
    queryset = DetalleCompra.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('compra',)