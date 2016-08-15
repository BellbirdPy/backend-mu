from __future__ import unicode_literals

from django.db import models
from potrero.models import *
from establecimiento.models import *
from sanitacion.models import Vacunacion
from venta.models import Venta

# Create your models here.
class Lote(models.Model):
    CHOICES_ESTADO = (
        ("V", "Vendido"),
        ("N", "Normal"),
    )
    estado = models.CharField(max_length=1, choices=CHOICES_ESTADO, default="N")
    nombre = models.CharField(max_length=80)
    potrero = models.OneToOneField(Potrero,related_name='lote',null=True,blank=True)
    peso_promedio = models.FloatField(blank=True, null=True)
    establecimiento = models.ForeignKey(Establecimiento,related_name='lotes')
    is_venta = models.BooleanField(default=False)
    venta = models.ForeignKey(Venta,related_name='lotes',on_delete=models.SET_NULL,null=True,default=None)
    vacunacion = models.ManyToManyField(Vacunacion, related_name='lotes', default=None, blank=True)


    def __unicode__(self):
        return unicode(self.nombre)