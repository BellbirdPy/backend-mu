from rest_framework import serializers
from models import *


class AnimalSerializer(serializers.ModelSerializer):
    raza_nombre = serializers.CharField(source='raza.nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    estado_sanitario_display = serializers.CharField(source='get_estado_sanitario_display', read_only=True)
    lote_nombre = serializers.CharField(source='lote.nombre', read_only=True)

    class Meta:
        model = Animal
        fields = ['id', 'caravana', 'lote', 'lote_nombre', 'establecimiento', 'raza', 'categoria', 'raza_nombre',
                  'categoria_nombre', 'carimbo', 'estado_sanitario_display', 'estado_sanitario', 'peso_especifico',
                  'origen','detalle_compra']
