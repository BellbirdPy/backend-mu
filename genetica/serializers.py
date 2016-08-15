from rest_framework import serializers

from animal.serializers import AnimalSerializer
from lote.serializers import LoteSerializer
from models import *


class LoteGeneticaSerializer(serializers.ModelSerializer):
    lote = LoteSerializer(many=False, read_only=True)

    class Meta:
        model = LoteGenetica
        fields = ['id', 'lote', 'raza', 'categoria', 'porcentaje_pureza', 'tipo_servicio', 'carimbo', 'descripcion',
                  'pedigree_padre']


class AnimalGeneticaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(many=False, read_only=True)

    class Meta:
        model = AnimalGenetica
        fields = ['id', 'animal', 'raza', 'categoria', 'porcentaje_pureza', 'tipo_servicio', 'carimbo', 'rp',
                  'descripcion', 'cantidad_pajuelas', 'pedigree_padre', 'pedigree_madre', 'pedigree_abuelo']
