from rest_framework import viewsets,filters
from serializers import *
from models import *
# Create your views here.

class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = LoteSerializer
    queryset = Lote.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('establecimiento',)
