import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_fields = ('establecimiento','estado','lote','categoria','raza','carimbo','estado_sanitario','caravana')
    ordering_fields = '__all__'
    ordering = ('caravana',)

    def create(self, request, *args, **kwargs):
        if 'animales' in request.data:
            animales = request.data['animales']
            serializer = self.get_serializer(data=animales, many=True)
            if serializer.is_valid():
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED,
                                headers=headers)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super(AnimalViewSet, self).create(request,*args, **kwargs)

@login_required(None,'login','/login/')
def list_caravana_animal(request,pk):
    try:
        user = request.user
        establecimiento = Establecimiento.objects.get(Q(owner=user) and Q(id=pk) | Q(miembros=user) and Q(id=pk))
        animales = list(establecimiento.animales.all().values_list('caravana',flat=True))
        some_data_to_dump = {'animales': animales}
        print animales
    except:
        some_data_to_dump = {'animales': []}

    data = json.dumps(some_data_to_dump)


    return HttpResponse(data, content_type='application/json')

