from rest_framework import serializers
from models import *

class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento

class EventoEstablecimientoSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_tit',read_only=True)
    start2 = serializers.DateTimeField(source='start',read_only=True)
    end2 = serializers.DateTimeField(source='end',read_only=True)


    class Meta:
        model = EventoEstablecimiento
        fields = ['id','color','start','end','title','nombre','establecimiento','veterinario','allDay','start2','end2']

    def get_tit(self, obj):
        return obj.nombre + ' - Veterinario: ' + obj.veterinario
