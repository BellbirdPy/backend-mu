from rest_framework import serializers
from models import *
from animal.models import Animal
from animal.serializers import AnimalSerializer

class LoteSerializer(serializers.ModelSerializer):
    potrero_nombre = serializers.CharField(source='potrero.nombre',read_only=True)

    class Meta:
        model = Lote
        fields = ['id','nombre','potrero','potrero_nombre','peso_promedio','establecimiento','venta','cantidad']

        def create(self, validated_data):
            if validated_data.has_key('animales'):
                animales = validated_data.pop('animales')
                lote = Lote.objects.create(**validated_data)
                for animal in animales:
                    animal.lote = lote
                    animal.save()
            else:
                lote = Lote.objects.create(**validated_data)
            return lote

class LoteAnimalCompletoSerializer(serializers.ModelSerializer):
    animales_completo = AnimalSerializer(source='animales',many=True,read_only=True)

    class Meta:
        model = Lote
        fields = ['id','animales_completo']