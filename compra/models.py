from __future__ import unicode_literals

from configuracion.models import Categoria, Raza
from django.db import models
from establecimiento.models import Establecimiento

# Create your models here.
from lote.models import Lote


class Compra(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="compras")
    cod_establecimiento_vendedor = models.CharField(max_length=32)
    nombre_vendedor = models.CharField(max_length=100)
    numero_guia = models.IntegerField()
    fecha_compra = models.DateField()
    precio_total = models.BigIntegerField(blank=True, null=True, default=0)
    fecha_creacion = models.DateField(auto_now=True)

    def __unicode__(self):
        return unicode(self.cod_establecimiento_vendedor + ' ' + self.nombre_vendedor + ' '
                       + self.fecha_compra.strftime('%d-%m-%Y'))


class DetalleCompra(models.Model):
    carimbo = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    caravana_inicial = models.PositiveIntegerField(default=0)

    compra = models.ForeignKey(Compra, related_name="detalle_compra", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL, related_name="detalle_compra")
    raza = models.ForeignKey(Raza, null=True, on_delete=models.SET_NULL, related_name="detalle_compra")
    lote = models.ForeignKey(Lote, null=True, on_delete=models.SET_NULL, related_name="detalle_compra")

    def __unicode__(self):
        return unicode(self.categoria.nombre + ' ' + self.cantidad.__str__())
