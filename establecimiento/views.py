from rest_framework import viewsets, filters
from serializers import *
from models import *
from django.db.models import Q
# Create your views here.

class EstablecimientoViewSet(viewsets.ModelViewSet):
    serializer_class = EstablecimientoSerializer

    def get_queryset(self):
        """
            This view should return a list of all the purchases
            for the currently authenticated user.
            """
        return Establecimiento.objects.filter(Q(owner=self.request.user) | Q(miembros=self.request.user))