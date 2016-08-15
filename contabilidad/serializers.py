from rest_framework import serializers
from models import *

class EgresoSerializer(serializers.ModelSerializer):
    rubro_display = serializers.CharField(source='get_rubro_display', read_only=True)
    class Meta:
        model = Egreso
        fields = ('id','fecha','descripcion', 'rubro', 'monto','establecimiento', 'rubro_display')



class IngresoVarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngresoVario
        fields = ('id','fecha','motivo', 'comprador', 'cantidad','establecimiento', 'precio_unitario')

class IngresoVentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngresoVenta
        fields = ('id', 'fecha', 'comprador', 'cantidad', 'total', 'establecimiento', 'carimbo', 'categoria', 'peso_promedio')