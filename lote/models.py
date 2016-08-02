from __future__ import unicode_literals

from django.db import models
from potrero.models import *
from establecimiento.models import *
from venta.models import Venta
from servicio.models import Servicio

# Create your models here.
class Lote(models.Model):
    CHOICES_ESTADO = (
        ("V", "Vendido"),
        ("N", "Normal"),
    )
    estado = models.CharField(max_length=1, choices=CHOICES_ESTADO, default="N")
    nombre = models.CharField(max_length=80)
    potrero = models.OneToOneField(Potrero,related_name='lote')
    peso_promedio = models.FloatField(blank=True, null=True)
    establecimiento = models.ForeignKey(Establecimiento,related_name='lotes')
    is_venta = models.BooleanField(default=False)
    venta = models.ForeignKey(Venta,related_name='lotes',on_delete=models.SET_NULL,null=True,default=None)
    servicio = models.ForeignKey(Servicio, related_name='lotes', on_delete=models.SET_NULL, null=True, default=None)

    def __unicode__(self):
        return unicode(self.nombre)