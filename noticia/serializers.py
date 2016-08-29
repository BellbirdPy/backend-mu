from rest_framework import serializers
from models import *


class NoticiaSerializer(serializers.ModelSerializer):


    class Meta:
        model = Noticia

