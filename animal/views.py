import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import viewsets, filters, status, generics
from rest_framework.decorators import list_route
from rest_framework.response import Response
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.



class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_fields = ('palpaciones','establecimiento','estado','lote','categoria','categoria__codigo','categoria__is_hembra','prenada','raza','carimbo','estado_sanitario','venta')
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

    def update(self, request, *args, **kwargs):
        if 'animales' in request.data:
            animales = request.data['animales']
            instance = []
            for a in animales:
                viejo = Animal.objects.get(id=a['id']) or None
                if viejo:
                    instance.append(viejo)
            serializer = self.get_serializer(data=animales, many=True)
            if serializer.is_valid():
                serializer.update(instance,serializer.validated_data)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED,
                                headers=headers)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super(AnimalViewSet, self).update(request, *args, **kwargs)





