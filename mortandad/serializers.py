from rest_framework import serializers
from models import *

class MortandadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mortandad
        fields = ['id','fecha','tipo','razon','establecimiento','animales']
