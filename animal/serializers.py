from rest_framework import serializers
from models import *

class AnimalListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        animales = [Animal(**item) for item in validated_data]
        return Animal.objects.bulk_create(animales)

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        animal_mapping = {animal.id: animal for animal in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for animal_id, data in data_mapping.items():
            animal = animal_mapping.get(animal_id, None)
            if animal is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(animal, data))

        # Perform deletions.
        #for animal_id, animal in animal_mapping.items():
        #    if animal_id not in data_mapping:
        #        animal.delete()

        return ret





class AnimalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    raza_nombre = serializers.CharField(source='raza.nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    estado_sanitario_display = serializers.CharField(source='get_estado_sanitario_display', read_only=True)
    lote_nombre = serializers.CharField(source='lote.nombre', read_only=True)


    class Meta:
        model = Animal
        list_serializer_class = AnimalListSerializer
        fields = ['id', 'caravana', 'lote', 'lote_nombre', 'establecimiento', 'raza', 'categoria', 'raza_nombre',
                  'categoria_nombre', 'carimbo', 'estado_sanitario_display', 'estado_sanitario', 'peso_especifico',
                  'origen','detalle_compra','estado','venta','prenada','caravana_madre']


