from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from establecimiento.models import Establecimiento
from django.db.models import Max
# Generates a "SELECT MAX..." statement


# Create your models here.
class Potrero(models.Model):
    codigo = models.PositiveIntegerField(null=True,default=None)
    nombre = models.CharField(max_length=100)
    superficie = models.PositiveIntegerField(blank=True,null=True)
    descripcion = models.CharField(max_length=200,blank=True,null=True)
    uso = models.TextField(null=True,blank=True)
    establecimiento = models.ForeignKey(Establecimiento,related_name='potreros')
    fecha_creacion = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ('establecimiento','codigo')

    def __unicode__(self):
        return unicode(self.nombre)
