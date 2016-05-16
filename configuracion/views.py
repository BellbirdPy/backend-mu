from rest_framework import viewsets
from serializers import *
from models import *
# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class RazaViewSet(viewsets.ModelViewSet):
    serializer_class = RazaSerializer
    queryset = Raza.objects.all()
