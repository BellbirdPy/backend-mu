from __future__ import unicode_literals

from django.db import models
from potrero.models import *
from establecimiento.models import *

# Create your models here.
class Lote(models.Model):
    nombre = models.CharField(max_length=80)
    potrero = models.OneToOneField(Potrero,related_name='lote')
    peso_promedio = models.FloatField(blank=True, null=True)
    establecimiento = models.ForeignKey(Establecimiento,related_name='lotes')
    is_venta = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.nombre)