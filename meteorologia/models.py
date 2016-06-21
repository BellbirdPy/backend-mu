from __future__ import unicode_literals
from establecimiento.models import Establecimiento
from django.db import models

# Create your models here.
class Registro(models.Model):
    fecha = models.DateTimeField()
    cantidad = models.FloatField()
    establecimiento = models.ForeignKey(Establecimiento,related_name='registros')

    def __unicode__(self):
        return unicode(self.fecha)

