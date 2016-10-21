from __future__ import unicode_literals

from establecimiento.models import Establecimiento
from django.db import models

# Create your models here.
class Evento(models.Model):
    title = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=7,default='')
    allDay = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.title)

class EventoEstablecimiento(models.Model):
    nombre = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=7, default='#CDDC39')
    veterinario = models.TextField()
    establecimiento = models.ForeignKey(Establecimiento,related_name='eventos')
    allDay = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now=True)



    def __unicode__(self):
        return unicode(self.nombre)

class Vacunacion(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="vacunaciones")
    fecha_vacunacion = models.DateField()
    nombre = models.CharField(max_length=50, default='')
    nombre_cientifico = models.CharField(max_length=50, default='',blank=True, null=True)
    veterinario = models.CharField(max_length=40, default='')
    enfermedad = models.CharField(max_length=30,default='')
    codigo = models.CharField(max_length=20,default='',blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return unicode(self.nombre)
