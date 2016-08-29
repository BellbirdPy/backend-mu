from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer
from animal.serializers import AnimalSerializer

class ServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicio
        fields = ['id', 'establecimiento', 'fecha_inicio', 'fecha_fin', 'tipo',
                  'lotes']

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
            l.servicio = servicio
            l.save()
        return servicio
