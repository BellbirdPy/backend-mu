from __future__ import unicode_literals

from django.db import models
from establecimiento.models import Establecimiento
from lote.models import Lote

# Create your models here.
class Servicio(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="servicios",default=None,null=True)
    CHOICES_TIPO = (
        ("N","Monta Natural"),
        ("I","Inseminacion Artificial")
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.CharField(max_length=1,choices=CHOICES_TIPO,default="N")
    lote = models.ForeignKey(Lote,related_name='servicios')
    cantidad_toros = models.IntegerField(default=0)


    def __unicode__(self):
        return unicode(self.tipo) + unicode(self.fecha)