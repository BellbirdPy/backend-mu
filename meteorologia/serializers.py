from rest_framework import serializers
from models import *

class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registro
        fields = ('id','fecha','cantidad','establecimiento')
