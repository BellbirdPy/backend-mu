from __future__ import unicode_literals

from compra.models import DetalleCompra
from django.db import models
from configuracion.models import *
from django.db.models import signals
from lote.models import *
from establecimiento.models import *
from mortandad.models import *
from venta.models import Venta
from servicio.models import Servicio
from lote.signals import count_animales
# Create your models here.
class Animal(models.Model):
    CHOICES_ESTADO = (
        ("V", "Vivo"),
        ("M", "Muerto"),
        ("E", "Eliminado"),
        ("S", "Vendido")
    )
    CHOICES_SANITARIO = (
        ("E", "En fecha"),
        ("N", "No esta en fecha"),
        ("D", "Desconocido")
    )
    CHOICES_ORIGEN = (
        ("C", "Compra"),
        ("N", "Nacimiento"),
        ("S", "Carga de sistema")
    )

    estado = models.CharField(max_length=1, choices=CHOICES_ESTADO, default="V")
    caravana = models.CharField(max_length=8, blank=True,default='')
    caravana_madre = models.CharField(max_length=8,blank=True,default='')
    carimbo = models.PositiveIntegerField()
    prenada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, related_name="animales", null=True, on_delete=models.SET_NULL)
    raza = models.ForeignKey(Raza, related_name="animales", null=True, on_delete=models.SET_NULL )
    estado_sanitario = models.CharField(max_length=1, choices=CHOICES_SANITARIO, default="E")
    peso_especifico = models.FloatField(null=True,blank=True)
    is_hembra = models.BooleanField(default=False)
    lote = models.ForeignKey(Lote, related_name="animales", null=True, on_delete=models.SET_NULL)
    mortandad = models.ForeignKey(Mortandad, related_name="animales", null=True, on_delete=models.SET_NULL)
    establecimiento = models.ForeignKey(Establecimiento,related_name="animales")

    origen = models.CharField(max_length=1, choices=CHOICES_ORIGEN, default="S")
    detalle_compra = models.ForeignKey(DetalleCompra,related_name="animales",null=True, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta,related_name="animales",null=True,on_delete=models.SET_NULL,default=None)
    vacunacion = models.ManyToManyField(Vacunacion, related_name='animales',blank=True, default=None)
    servicio = models.ManyToManyField(Servicio,related_name='toros',blank=True,default=None)
    fecha_creacion = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return unicode(self.caravana) +" - " +unicode(self.categoria)+" - " +unicode(self.raza)

signals.post_save.connect(count_animales, sender=Animal)
signals.post_delete.connect(count_animales, sender=Animal)