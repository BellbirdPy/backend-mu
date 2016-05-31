from models import *
from rest_framework import serializers


class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establecimiento
