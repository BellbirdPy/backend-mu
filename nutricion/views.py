from rest_framework import viewsets,filters
from serializers import *
from models import *
# Create your views here.

class NutricionViewSet(viewsets.ModelViewSet):
    serializer_class = NutricionSerializer
    queryset = Nutricion.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('establecimiento',)
