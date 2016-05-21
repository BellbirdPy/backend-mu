from rest_framework import serializers
from models import *


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'establecimiento', 'cod_establecimiento_vendedor', 'nombre_vendedor', 'fecha', 'detalle_compra']


class DetalleCompraSerialzer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = ['id', 'compra', 'categoria', 'carimbo', 'raza', 'cantidad', 'animales']
