from django.db.models import Q
from rest_framework import viewsets,filters
from rest_framework.response import Response
from serializers import *
from models import *
# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
    ordering = ('nombre',)

    def list(self, request):
        establecimiento = self.request.query_params.get('establecimiento', None)
        ordering = self.request.query_params.get('ordering', 'nombre')
        queryset = Categoria.objects.filter(Q(establecimiento=establecimiento) | Q(establecimiento=None)).order_by(ordering).distinct()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class RazaViewSet(viewsets.ModelViewSet):
    serializer_class = RazaSerializer
    filter_backends = (filters.OrderingFilter,)
    queryset = Raza.objects.all()
    ordering_fields = '__all__'
    ordering = ('nombre',)

    def list(self, request):
        establecimiento = self.request.query_params.get('establecimiento', None)
        ordering = self.request.query_params.get('ordering', 'nombre')
        queryset = Raza.objects.filter(Q(establecimiento=establecimiento) | Q(establecimiento=None)).order_by(ordering).distinct()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
