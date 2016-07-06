from rest_framework import viewsets,filters
from serializers import *
from models import *

# Create your views here.
class NoticiaViewSet(viewsets.ModelViewSet):
    serializer_class = NoticiaSerializer
    queryset = Noticia.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = '__all__'
    ordering = ('-fecha',)

