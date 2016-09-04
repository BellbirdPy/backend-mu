from rest_framework import serializers
from models import *
from animal.serializers import AnimalSerializer
from rest_framework.response import Response


class MortandadSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    animales_completo = AnimalSerializer(source='animales',many=True,read_only=True)

    class Meta:
        model = Mortandad
        fields = ['id','fecha','tipo','razon','establecimiento','animales','tipo_display','animales_completo']

    def create(self, validated_data):
        animales = validated_data.pop('animales')
        mortandad = Mortandad.objects.create(**validated_data)
        for animal in animales:
            animal.estado = 'M'
            animal.mortandad = mortandad
            animal.save()
        return mortandad





