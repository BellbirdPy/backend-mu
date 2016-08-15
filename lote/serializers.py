from rest_framework import serializers
from models import *
from animal.models import Animal
from animal.serializers import AnimalSerializer

class LoteSerializer(serializers.ModelSerializer):
    potrero_nombre = serializers.CharField(source='potrero.nombre',read_only=True)

    class Meta:
        model = Lote
        fields = ['id','nombre','potrero','potrero_nombre','animales','peso_promedio','establecimiento','venta']

class LoteAnimalCompletoSerializer(serializers.ModelSerializer):
    animales_completo = AnimalSerializer(source='animales',many=True,read_only=True)

    class Meta:
        model = Lote
        fields = ['id','animales_completo']