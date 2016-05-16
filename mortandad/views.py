from rest_framework import viewsets,filters
from serializers import *
from models import *
# Create your views here.

class MortandadViewSet(viewsets.ModelViewSet):
    serializer_class = MortandadSerializer
    queryset = Mortandad.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('establecimiento',)
