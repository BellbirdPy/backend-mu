#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone
from django.db import models

from configuracion.models import Categoria
from establecimiento.models import Establecimiento


class Egreso(models.Model):
    CHOICES_RUBRO = (
        ('GD', 'Gastos Directos'),
        ('GA','Gastos Administrativos'),
        ('IT','Impuestos y Tazas'),
        ('GC','Gastos de Comercialización'),
        ('GF', 'Gastos Financieros')
    )
    fecha = models.DateField()
    descripcion = models.CharField(max_length=80, default='')
    rubro = models.CharField(max_length=2, choices=CHOICES_RUBRO, default='GD')
    monto = models.PositiveIntegerField()
    establecimiento = models.ForeignKey(Establecimiento, related_name='egreso')

    def __unicode__(self):
        return unicode(self.descripcion)


class IngresoVario(models.Model):

    fecha = models.DateField()
    motivo = models.CharField(max_length=80, default='')
    comprador = models.CharField(max_length=80, default='')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()
    establecimiento = models.ForeignKey(Establecimiento, related_name='ingreso_vario')


    def __unicode__(self):
        return unicode(self.motivo)


class IngresoVenta(models.Model):

    fecha = models.DateField()
    comprador = models.CharField(max_length=80, default='')
    cantidad = models.PositiveIntegerField()
    categoria = models.CharField(max_length=80)
    carimbo = models.PositiveIntegerField ()
    peso_promedio = models.FloatField(blank=True, null=True)
    total = models.PositiveIntegerField()
    establecimiento = models.ForeignKey(Establecimiento, related_name='ingreso_venta')

    def __unicode__(self):
        return unicode(self.comprador+''+self.fecha.strftime('%d-%m-%Y'))
