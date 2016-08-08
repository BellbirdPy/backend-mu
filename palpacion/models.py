from __future__ import unicode_literals
from establecimiento.models import Establecimiento
from servicio.models import Servicio
from animal.models import Animal
from django.db import models

# Create your models here.
class Palpacion(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="palpaciones")
    servicio = models.ForeignKey(Servicio, related_name="palpaciones")
    metodo_manual = models.BooleanField(default=True)
    fecha = models.DateField()


    def __unicode__(self):
        return unicode(self.fecha) + unicode(self.metodo_manual)

class DetallePalpacion(models.Model):
    palpacion = models.ForeignKey(Palpacion, related_name="detalles")
    animal = models.ForeignKey(Animal,related_name="palpaciones")
    resultado = models.BooleanField()
    gestacion = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return unicode(self.animal) + unicode(self.resultado)

