from rest_framework import serializers
from models import *
from servicio.serializers import ServicioSerializer

class DetallesPalpacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetallePalpacion
        fields = ['id', 'animal','resultado','gestacion']

class PalpacionSerializer(serializers.ModelSerializer):
    cantidad_actual_prenados = serializers.IntegerField(source='get_animales_prenados',read_only=True)
    detalles = DetallesPalpacionSerializer(many=True,write_only=True)
    servicio_completo = ServicioSerializer(source='servicio',read_only=True)
    metodo_display = serializers.CharField(source='get_metodo_display', read_only=True)

    class Meta:
        model = Palpacion
        fields = ['id', 'establecimiento', 'fecha','metodo','metodo_display','servicio','servicio_completo','detalles','cantidad_prenados','cantidad_actual_prenados','cantidad_total','lote']

    def create(self, validated_data):
        detalles = validated_data.pop('detalles')
        palpacion = Palpacion.objects.create(**validated_data)
        print palpacion.lote
        for detalle in detalles:
            detalle_creado = DetallePalpacion.objects.create(palpacion=palpacion,**detalle)
            if detalle_creado.resultado == True:
                detalle_creado.animal.prenada = True
                detalle_creado.animal.palpaciones.add(palpacion)
                detalle_creado.animal.lote = palpacion.lote
                detalle_creado.animal.save()
            else:
                detalle_creado.animal.prenada = False
                detalle_creado.animal.save()
        palpacion.servicio.palpado = True
        palpacion.servicio.save()

        return palpacion


