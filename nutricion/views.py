from django_filters import MethodFilter
from rest_framework import viewsets,filters
from serializers import *
from models import *
# Create your views here.
ahora = timezone.now()
class NutricionViewSet(viewsets.ModelViewSet):
    serializer_class = NutricionSerializer
    queryset = Nutricion.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento','lotes','tipo_nutricion',)
    ordering_fields = '__all__'
    ordering = ('fecha_inicio',)
