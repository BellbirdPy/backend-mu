from __future__ import unicode_literals

from django.template.defaultfilters import register
from django.utils import timezone
from lote.models import *
from django.db import models

# Create your models here.
class Nutricion(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    lotes = models.ManyToManyField(Lote, related_name="nutriciones")
    tipo_nutricion = models.TextField()
    tipo_comida = models.TextField()
    descripcion_comida = models.TextField(null=True,blank=True)
    kilos = models.FloatField()
    establecimiento = models.ForeignKey(Establecimiento,related_name='nutriciones')
    fecha_creacion = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return unicode(self.tipo_nutricion)

    def is_activo(self):
        ahora = timezone.now()
        if ahora >= self.fecha_inicio and ahora <= self.fecha_fin:
            return True
        else:
            return False
