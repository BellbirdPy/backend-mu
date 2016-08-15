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
    
class VacunacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacunacion
        fields = ['id', 'establecimiento','fecha_vacunacion', 'nombre', 'nombre_cientifico',
                  'veterinario','enfermedad','codigo', 'lotes']

    def create(self, validated_data):
        try:
            lotes = validated_data.pop('lotes')
            print lotes
        except:
            lotes = []
            print "error"
        print validated_data
        vacunacion = Vacunacion.objects.create(**validated_data)

        for l in lotes:
            l.vacunacion.add(vacunacion)
            l.save()
            for a in l.animales.all():
                a.vacunacion.add(vacunacion)
                a.save()

        return vacunacion
