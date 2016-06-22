from rest_framework import serializers
from models import *
from lote.serializers import LoteSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class EmpleadoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Empleado



class ContratistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contratista