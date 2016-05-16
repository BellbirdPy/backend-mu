from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer

class NutricionSerializer(serializers.ModelSerializer):
    lotes_completo = LoteSerializer(source='lotes', many=True,read_only=True)

    class Meta:
        model = Nutricion
        fields = ('id','fecha_inicio','fecha_fin','tipo_nutricion','tipo_comida','descripcion_comida','lotes','lotes_completo','kilos','establecimiento')
