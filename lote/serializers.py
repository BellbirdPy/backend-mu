from rest_framework import serializers
from models import *

class LoteSerializer(serializers.ModelSerializer):
    potrero_nombre = serializers.CharField(source='potrero.nombre',read_only=True)

    class Meta:
        model = Lote
        fields = ['id','nombre','potrero','potrero_nombre','animales','peso_promedio','establecimiento']
