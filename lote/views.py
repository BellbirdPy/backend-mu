from rest_framework import viewsets,filters
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.

class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = LoteSerializer
    queryset = Lote.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, RelatedOrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('nombre',)
