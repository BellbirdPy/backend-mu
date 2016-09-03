from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

class EstablecimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establecimiento
        fields = ('id','nombre','owner','miembros','lotes','potreros')

class TareaSerializer(serializers.ModelSerializer):
    usuario_asignado_display = serializers.CharField(source='get_usuario_asignado_display', read_only=True)
    class Meta:
        model = Tarea
        fields = ('id', 'fecha', 'descripcion', 'usuario_asignado','usuario_asignado_display',
                  'leido','establecimiento', 'usuario_creador')

class MiembroSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name','establecimientos','establecimientos_owner','email')