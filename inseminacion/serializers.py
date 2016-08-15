from rest_framework import serializers
from models import *

class DetallesInseminacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleInseminacion
        fields = ['id', 'animal','pajuela']

class InseminacionSerializer(serializers.ModelSerializer):
    detalles = DetallesInseminacionSerializer(many=True)

    class Meta:
        model = Inseminacion
        fields = ['id', 'establecimiento', 'fecha','detalles']

    def create(self, validated_data):
        detalles = validated_data.pop('detalles')
        inseminacion = Inseminacion.objects.create(**validated_data)
        for detalle in detalles:
            DetalleInseminacion.objects.create(inseminacion=inseminacion,**detalle)
        return inseminacion


