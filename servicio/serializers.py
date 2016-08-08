from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer
from animal.serializers import AnimalSerializer

class ServicioSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    lotes_completo = LoteSerializer(source='lotes', many=True, read_only=True)

    class Meta:
        model = Servicio
        fields = ['id', 'establecimiento', 'fecha_inicio', 'fecha_fin', 'tipo','lotes','tipo_display','lotes_completo']

    def create(self, validated_data):
        try:
            lotes = validated_data.pop('lotes')
            print lotes
        except:
            lotes = []
            print "error"
        print validated_data
        servicio = Servicio.objects.create(**validated_data)
        for l in lotes:
            l.servicio.add(servicio)
            l.save()
        return servicio
