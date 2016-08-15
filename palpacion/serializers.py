from rest_framework import serializers
from models import *
from servicio.serializers import ServicioSerializer

class DetallesPalpacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetallePalpacion
        fields = ['id', 'animal','resultado','gestacion']

class PalpacionSerializer(serializers.ModelSerializer):
    detalles = DetallesPalpacionSerializer(many=True)
    servicio_completo = ServicioSerializer(source='servicio',read_only=True)
    metodo_display = serializers.CharField(source='get_metodo_display', read_only=True)

    class Meta:
        model = Palpacion
        fields = ['id', 'establecimiento', 'fecha','metodo','metodo_display','servicio','servicio_completo','detalles','cantidad_prenados','cantidad_total']

    def create(self, validated_data):
        detalles = validated_data.pop('detalles')
        palpacion = Palpacion.objects.create(**validated_data)
        for detalle in detalles:
            DetallePalpacion.objects.create(palpacion=palpacion,**detalle)
        return palpacion


