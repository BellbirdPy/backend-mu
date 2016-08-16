from rest_framework import serializers

from animal.serializers import AnimalSerializer
from configuracion.serializers import RazaSerializer, CategoriaSerializer
from lote.serializers import LoteSerializer
from models import *


class LoteGeneticaSerializer(serializers.ModelSerializer):
    lote = LoteSerializer(many=False, read_only=True)
    raza = RazaSerializer(many=False, read_only=True)
    categoria = CategoriaSerializer(many=False, read_only=True)

    class Meta:
        model = LoteGenetica
        fields = ['id', 'establecimiento', 'lote', 'raza', 'categoria', 'porcentaje_pureza', 'tipo_servicio',
                  'carimbo', 'descripcion', 'pedigree_padre']


class AnimalGeneticaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(many=False, read_only=True)

    class Meta:
        model = AnimalGenetica
        fields = ['id', 'establecimiento', 'animal', 'nombre', 'nombre_corto', 'porcentaje_pureza', 'tipo_servicio',
                  'rp', 'descripcion', 'cantidad_pajuelas', 'pedigree_padre', 'pedigree_madre', 'pedigree_abuelo']
