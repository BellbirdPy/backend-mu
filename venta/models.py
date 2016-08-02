from __future__ import unicode_literals

from django.db import models

# Create your models here.
from establecimiento.models import Establecimiento


class Venta(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="ventas")
    cod_establecimiento_comprador = models.CharField(max_length=32)
    nombre_comprador = models.CharField(max_length=100)
    numero_guia = models.IntegerField()
    fecha_venta = models.DateField()
    tipo_venta = models.CharField(max_length=10,default='lote')
    precio_total = models.BigIntegerField(blank=True, null=True, default=0)
    fecha_creacion = models.DateField(auto_now=True)

    def __unicode__(self):
        return unicode(self.cod_establecimiento_comprador + ' ' + self.nombre_comprador + ' '
                       + self.fecha_venta.strftime('%d-%m-%Y'))
