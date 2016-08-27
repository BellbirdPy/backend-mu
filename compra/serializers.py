from animal.models import Animal
from animal.serializers import AnimalSerializer
from lote.models import Lote
from models import *
from rest_framework import serializers


class DetalleCompraSerialzer(serializers.ModelSerializer):

    class Meta:
        model = DetalleCompra
        fields = ['id', 'categoria', 'carimbo', 'raza', 'cantidad', 'caravana_inicial', 'lote']


class CompraSerializer(serializers.ModelSerializer):
    detalle_compra = DetalleCompraSerialzer(many=True)

    class Meta:
        model = Compra
        fields = ['id', 'establecimiento','carga_masiva', 'cod_establecimiento_vendedor', 'nombre_vendedor', 'numero_guia',
                  'fecha_compra', 'precio_total', 'detalle_compra']

    def create(self, validated_data):
        detalle_data = validated_data.pop('detalle_compra')
        compra = Compra.objects.create(**validated_data)
        for detalle in detalle_data:
            new_detalle_compra = DetalleCompra.objects.create(compra=compra, **detalle)
            lista = []
            if new_detalle_compra.lote:
                lote = new_detalle_compra.lote
            else:
                lote = None
            for i in range(new_detalle_compra.cantidad):
                a = Animal(caravana=new_detalle_compra.caravana_inicial + i,
                           carimbo=new_detalle_compra.carimbo,
                           categoria=Categoria.objects.get(id=new_detalle_compra.categoria_id),
                           raza=Raza.objects.get(id=new_detalle_compra.raza_id),
                           lote=lote,
                           establecimiento=Establecimiento.objects.get(id=compra.establecimiento_id),
                           detalle_compra=new_detalle_compra)
                lista.append(a)

            Animal.objects.bulk_create(lista)
            if new_detalle_compra.lote:
                new_detalle_compra.lote.count_animales()

        return compra
