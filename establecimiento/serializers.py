from rest_framework import serializers

from models import *
from django.contrib.auth.models import User


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nombre')


class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ciudad
        fields = ('id', 'nombre')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username')


class EstablecimientoSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.CharField(source='departamento.nombre', read_only=True)
    owner = UserSerializer()
    current_user = serializers.SerializerMethodField('_user')

    # Use this method for the custom field
    def _user(self, obj):
        user = self.context['request'].user
        return user.id

    class Meta:
        model = Establecimiento
        fields = ('id', 'nombre', 'codigo', 'departamento', 'departamento_nombre', 'ciudad', 'owner',
                  'miembros', 'lotes', 'potreros', 'estado', 'plan','current_user')


class TareaSerializer(serializers.ModelSerializer):
    usuario_asignado_display = serializers.CharField(source='get_usuario_asignado_display', read_only=True)

    class Meta:
        model = Tarea
        fields = ('id', 'fecha', 'descripcion', 'usuario_asignado', 'usuario_asignado_display',
                  'leido', 'establecimiento', 'usuario_creador')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class MiembroSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cargo_display = serializers.CharField(source='get_cargo_display', read_only=True)

    class Meta:
        model = Miembro
        fields = ('id', 'user', 'cargo', 'telefono', 'cargo_display', 'establecimiento')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = User.objects.create_user(**user_data)
        miembro = Miembro.objects.create(user=new_user, **validated_data)

        return miembro
