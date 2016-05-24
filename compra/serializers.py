from animal.models import Animal
from animal.serializers import AnimalSerializer
from configuracion.serializers import CategoriaSerializer, RazaSerializer
from rest_framework import serializers
from models import *


class DetalleCompraSerialzer(serializers.ModelSerializer):
    animales = AnimalSerializer(many=True, read_only=True)

    class Meta:
        model = DetalleCompra
        fields = ['id', 'categoria', 'carimbo', 'raza', 'cantidad', 'caravana_inicial', 'animales']


class CompraSerializer(serializers.ModelSerializer):
    detalle_compra = DetalleCompraSerialzer(many=True)

    class Meta:
        model = Compra
        fields = ['id', 'establecimiento', 'cod_establecimiento_vendedor', 'nombre_vendedor', 'fecha', 'detalle_compra']

    def create(self, validated_data):
        detalle_data = validated_data.pop('detalle_compra')
        compra = Compra.objects.create(**validated_data)
        for detalle in detalle_data:
            new_detalle_compra = DetalleCompra.objects.create(compra=compra, **detalle)
            for i in range(new_detalle_compra.cantidad):
                a = Animal(caravana=new_detalle_compra.caravana_inicial + i,
                           carimbo=new_detalle_compra.carimbo,
                           categoria=Categoria.objects.get(id=new_detalle_compra.categoria_id),
                           raza=Raza.objects.get(id=new_detalle_compra.raza_id),
                           establecimiento=Establecimiento.objects.get(id=compra.establecimiento_id),
                           detalle_compra=new_detalle_compra)
                a.save()
        return compra
