from rest_framework import viewsets, filters
from serializers import *
from models import *
# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('establecimiento',)
