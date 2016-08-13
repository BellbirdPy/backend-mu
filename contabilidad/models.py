#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone
from django.db import models

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
    monto = models.IntegerField()
    establecimiento = models.ForeignKey(Establecimiento, related_name='egreso')

    def __unicode__(self):
        return unicode(self.descripcion)


class IngresoVario(models.Model):

    fecha = models.DateField()
    motivo = models.CharField(max_length=80, default='')
    comprador = models.CharField(max_length=80, default='')
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    establecimiento = models.ForeignKey(Establecimiento, related_name='ingreso_vario')


    def __unicode__(self):
        return unicode(self.motivo)