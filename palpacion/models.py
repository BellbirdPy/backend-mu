from __future__ import unicode_literals
from establecimiento.models import Establecimiento
from servicio.models import Servicio
from animal.models import Animal
from lote.models import Lote
from django.db import models
from lote.models import Lote
# Create your models here.
class Palpacion(models.Model):
    CHOICES_METODO = (
        ("M", "Manual"),
        ("E", "Ecografo")
    )
    establecimiento = models.ForeignKey(Establecimiento, related_name="palpaciones")
    servicio = models.ForeignKey(Servicio, related_name="palpaciones")
    metodo = models.CharField(max_length=1, choices=CHOICES_METODO, default="M")
    fecha = models.DateField()
    cantidad_prenados = models.IntegerField()
    cantidad_total = models.IntegerField()
    animales_prenados = models.ManyToManyField(Animal,related_name='palpaciones')
    lote = models.ForeignKey(Lote,related_name='palpaciones',null=True,default=None)



    def __unicode__(self):
        return unicode(self.fecha) + unicode(self.metodo)

class DetallePalpacion(models.Model):
    palpacion = models.ForeignKey(Palpacion, related_name="detalles")
    animal = models.ForeignKey(Animal,related_name="detalle_palpaciones")
    resultado = models.BooleanField()
    gestacion = models.CharField(max_length=8,null=True,blank=True)

    def __unicode__(self):
        return unicode(self.animal) + unicode(self.resultado)

