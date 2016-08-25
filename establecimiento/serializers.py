from rest_framework import serializers
from models import *

class EstablecimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establecimiento
        fields = ('id','nombre','owner','miembros','lotes','potreros')

class TareaSerializer(serializers.ModelSerializer):
    usuario_asignado_display = serializers.CharField(source='get_usuario_asignado_display', read_only=True)
    class Meta:
        model = Tarea
        fields = ('id', 'fecha', 'descripcion', 'usuario_asignado','usuario_asignado_display',
                  'establecimiento', 'usuario_creador')

