from __future__ import unicode_literals

from django.db import models
from potrero.models import *
from establecimiento.models import *
from sanitacion.models import Vacunacion
from venta.models import Venta
import datetime

# Create your models here.
class Lote(models.Model):
    CHOICES_ESTADO = (
        ("V", "Vendido"),
        ("N", "Normal"),
    )
    estado = models.CharField(max_length=1, choices=CHOICES_ESTADO, default="N")
    nombre = models.CharField(max_length=80)
    potrero = models.ForeignKey(Potrero,related_name='lote',null=True,blank=True)
    peso_promedio = models.FloatField(blank=True, null=True)
    establecimiento = models.ForeignKey(Establecimiento,related_name='lotes')
    is_venta = models.BooleanField(default=False)
    venta = models.ForeignKey(Venta,related_name='lotes',on_delete=models.SET_NULL,null=True,default=None)
    vacunacion = models.ManyToManyField(Vacunacion, related_name='lotes', default=None, blank=True)
    cantidad = models.IntegerField(default=0,editable=False)

    fecha_creacion = models.DateTimeField(auto_now=True)

    def count_animales(self):
        """
        Counts the total number of live changes of this type and saves the result to the `change_count` field.
        """
        count = self.animales.filter(estado='V').count()
        self.cantidad = count
        self.save()

    def get_servicio_actual(self):
        fecha_hoy = datetime.date.today()
        servicios = self.servicios.filter(fecha_fin__gte=fecha_hoy,fecha_inicio__lte=fecha_hoy)
        if servicios:
            return servicios[0].get_tipo_display()

    def get_nutricion_actual(self):
        fecha_hoy = datetime.date.today()
        nutriciones = self.nutriciones.filter(fecha_fin__gte=fecha_hoy, fecha_inicio__lte=fecha_hoy)
        if nutriciones:
            return nutriciones[0].tipo_nutricion


    def __unicode__(self):
        return unicode(self.nombre)