from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer

class NutricionSerializer(serializers.ModelSerializer):
    lotes_completo = LoteSerializer(source='lotes', many=True,read_only=True)
    racion_diaria = serializers.SerializerMethodField('get_racion', read_only=True)

    def get_racion(self,obj):
        delta = obj.fecha_fin - obj.fecha_inicio
        dias = delta.days
        if dias > 0:
            racion = obj.kilos  /dias *1000
        else:
            racion = 0
        return racion



    class Meta:
        model = Nutricion
        fields = ('id','fecha_inicio','fecha_fin','tipo_nutricion','tipo_comida','descripcion_comida','lotes','lotes_completo','kilos','establecimiento','racion_diaria')
