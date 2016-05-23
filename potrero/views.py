from rest_framework import viewsets,filters
from serializers import *
from models import *
# Create your views here.

class PotreroViewSet(viewsets.ModelViewSet):
    serializer_class = PotreroSerializer
    queryset = Potrero.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento','lote')
    ordering_fields = '__all__'
    ordering = ('nombre',)
