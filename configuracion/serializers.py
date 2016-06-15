from rest_framework import serializers
from models import *

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id','codigo','nombre','is_hembra','establecimiento')

class RazaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raza
