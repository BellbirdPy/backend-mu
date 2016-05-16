from rest_framework import serializers
from models import *

class PotreroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Potrero
