from __future__ import unicode_literals

from django.db import models
from establecimiento.models import Establecimiento
from palpacion.models import Palpacion
from animal.models import Animal
from lote.models import Lote

# Create your models here.
class Paricion(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="pariciones")
    palpacion = models.ForeignKey(Palpacion, related_name="pariciones")
    fecha = models.DateField()
    madre = models.ForeignKey(Animal,related_name='pariciones')
    hijo = models.OneToOneField(Animal,related_name='nacimiento',null=True,blank=True)
    aborto = models.BooleanField(default=False)
    lote = models.ForeignKey(Lote,related_name='pariciones',null=True,blank=True)

    def __unicode__(self):
        return unicode(self.fecha) + unicode(self.madre)

