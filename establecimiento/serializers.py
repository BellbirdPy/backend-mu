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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name','email','password')


class MiembroSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cargo_display = serializers.CharField(source='get_cargo_display',read_only=True)


    class Meta:
        model = Miembro
        fields = ('id', 'user','cargo','cargo_display','establecimiento')


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = User.objects.create_user(**user_data)
        miembro = Miembro.objects.create(user=new_user,**validated_data)

        return miembro
