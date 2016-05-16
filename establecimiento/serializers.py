from rest_framework import serializers
from models import *

class EstablecimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establecimiento
