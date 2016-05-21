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


    def __unicode__(self):
        return unicode(self.nombre)
