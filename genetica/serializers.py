from rest_framework import serializers

from animal.serializers import AnimalSerializer
from models import *


class LoteGeneticaSerializer(serializers.ModelSerializer):
    lote_nombre = serializers.CharField(source='lote.nombre', read_only=True)
    raza_nombre = serializers.CharField(source='raza.nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = LoteGenetica
        fields = ['id', 'establecimiento', 'lote', 'lote_nombre', 'raza', 'raza_nombre', 'categoria',
                  'categoria_nombre', 'porcentaje_pureza', 'tipo_servicio',
                  'carimbo', 'descripcion', 'pedigree_padre']

    def create(self, validated_data):
        loteGenetica = LoteGenetica.objects.create(**validated_data)
        lote = Lote.objects.get(id=loteGenetica.lote_id)
        animales = Animal.objects.all().filter(lote=lote)
        i = 0
        for animal in animales:
            a = AnimalGenetica(establecimiento=loteGenetica.establecimiento,
                               animal=animal,
                               porcentaje_pureza=loteGenetica.porcentaje_pureza,
                               tipo_servicio=loteGenetica.tipo_servicio,
                               descripcion=loteGenetica.descripcion,
                               pedigree_padre=loteGenetica.pedigree_padre)
            a.save()
            i = i + 1
            print i, 'Listo: animal ', animal.id
        return loteGenetica


class AnimalGeneticaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(many=False, read_only=True)

    class Meta:
        model = AnimalGenetica
        fields = ['id', 'establecimiento', 'animal', 'nombre', 'nombre_corto', 'porcentaje_pureza', 'tipo_servicio',
                  'rp', 'descripcion', 'cantidad_pajuelas', 'pedigree_padre', 'pedigree_madre', 'pedigree_abuelo']
