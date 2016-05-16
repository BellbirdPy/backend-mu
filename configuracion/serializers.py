from rest_framework import serializers
from models import *

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria

class RazaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raza
