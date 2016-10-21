from __future__ import unicode_literals
from establecimiento.models import Establecimiento
from servicio.models import Servicio
from animal.models import Animal
from django.db import models
from configuracion.models import Pajuela

# Create your models here.
class Inseminacion(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="inseminaciones")
    servicio = models.ForeignKey(Servicio, related_name="inseminaciones")
    fecha = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return unicode(self.fecha) + unicode(self.servicio)

class DetalleInseminacion(models.Model):
    inseminacion = models.ForeignKey(Inseminacion, related_name="detalles")
    animal = models.ForeignKey(Animal,related_name="inseminaciones")
    pajuela = models.ForeignKey(Pajuela, related_name="inseminaciones")
    fecha_creacion = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return unicode(self.animal) + unicode(self.pajuela)
