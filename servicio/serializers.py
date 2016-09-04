from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer
from animal.serializers import AnimalSerializer
from inseminacion.serializers import InseminacionSerializer
from inseminacion.models import Inseminacion,DetalleInseminacion
from animal.models import Animal

class ServicioListSerializer(serializers.ListSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'establecimiento', 'fecha_inicio', 'fecha_fin', 'tipo', 'tipo_display',
                  'lote_completo','cantidad_toros','palpado']


class ServicioSerializer(serializers.ModelSerializer):

    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    lote_completo = LoteSerializer(source='lote', read_only=True)
    inseminaciones = InseminacionSerializer(many=True,write_only=True)
    toros = serializers.PrimaryKeyRelatedField(many=True,queryset=Animal.objects.filter(categoria__codigo='TORO'),write_only=True)

    class Meta:
        model = Servicio
        fields = ['id', 'establecimiento','palpado', 'fecha_inicio', 'fecha_fin','toros', 'tipo','lote','tipo_display','lote_completo','inseminaciones','cantidad_toros']

    def create(self, validated_data):
        if validated_data.has_key('toros'):
            toros = validated_data.pop('toros')
            print toros
        else:
            toros = []

        if validated_data.has_key('inseminaciones'):
            inseminaciones = validated_data.pop('inseminaciones')
        else:
            inseminaciones = []


        servicio = Servicio.objects.create(**validated_data)
        servicio.cantidad_toros = toros.__len__()
        servicio.save()

        for i in inseminaciones:
            detalles = []
            if i.has_key('detalles'):
                detalles = i.pop('detalles')
            inseminacion = Inseminacion.objects.create(servicio=servicio,**i)
            for d in detalles:
                DetalleInseminacion.objects.create(inseminacion=inseminacion,**d)

        for t in toros:
            t.servicio.add(servicio)
            t.save()
        return servicio
