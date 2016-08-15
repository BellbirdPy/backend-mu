from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer
from animal.serializers import AnimalSerializer
from inseminacion.serializers import InseminacionSerializer
from inseminacion.models import Inseminacion,DetalleInseminacion

class ServicioSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    lote_completo = LoteSerializer(source='lote', read_only=True)
    inseminaciones = InseminacionSerializer(many=True)

    class Meta:
        model = Servicio
        fields = ['id', 'establecimiento', 'fecha_inicio', 'fecha_fin', 'tipo','lote','toros','tipo_display','lote_completo','inseminaciones']

    def create(self, validated_data):
        if validated_data.has_key('toros'):
            toros = validated_data.pop('toros')
        else:
            toros = []

        if validated_data.has_key('inseminaciones'):
            inseminaciones = validated_data.pop('inseminaciones')
        else:
            inseminaciones = []


        servicio = Servicio.objects.create(**validated_data)

        for i in inseminaciones:
            if i.has_key('detalles'):
                detalles = i.pop('detalles')
            inseminacion = Inseminacion.objects.create(servicio=servicio,**i)
            for d in detalles:
                DetalleInseminacion.objects.create(inseminacion=inseminacion,**d)

        for t in toros:
            t.servicio.add(servicio)
            t.save()
        return servicio
