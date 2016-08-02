from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer
from animal.serializers import AnimalSerializer

class VentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venta
        fields = ['id', 'establecimiento', 'cod_establecimiento_comprador', 'nombre_comprador', 'numero_guia',
                  'fecha_venta', 'precio_total','tipo_venta','lotes','animales']

    def create(self, validated_data):
        try:
            animales = validated_data.pop('animales')
            lotes = validated_data.pop('lotes')

            print animales
            print lotes
        except:
            animales = []
            lotes = []
            print "error"
        print validated_data
        venta = Venta.objects.create(**validated_data)
        if venta.tipo_venta == 'lote':
            for l in lotes:
                l.venta = venta
                l.estado = 'V'
                l.save()
                for a in l.animales.all():
                    a.venta = venta
                    a.estado = 'S'
                    a.save()
        else:
            if venta.tipo_venta == 'animal':
                for a in animales:
                    a.venta = venta
                    a.estado = 'S'
                    a.lote = None
                    a.save()
        return venta
