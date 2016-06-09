from rest_framework import serializers
from models import *
from configuracion.serializers import *

class EstablecimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establecimiento
        fields = ('id','nombre','owner','miembros','lotes','potreros')
