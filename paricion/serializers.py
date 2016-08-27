from rest_framework import serializers
from models import *
from servicio.serializers import ServicioSerializer
from animal.serializers import AnimalSerializer
from animal.models import Animal

class ParicionSerializer(serializers.ModelSerializer):
    hijo = AnimalSerializer()

    class Meta:
        model = Paricion
        fields = ['id', 'hijo','madre','fecha','establecimiento','palpacion','aborto','lote']

    def create(self, validated_data):
        hijo = validated_data.pop('hijo')
        paricion = Paricion.objects.create(**validated_data)
        animal_hijo = Animal.objects.create(lote=paricion.lote,**hijo)
        animal_hijo.caravana_madre = paricion.madre.caravana
        paricion.madre.lote = paricion.lote
        paricion.madre.prenada = False
        paricion.hijo = animal_hijo
        paricion.save()
        paricion.madre.save()

        return paricion


