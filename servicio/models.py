from __future__ import unicode_literals

from django.db import models
from establecimiento.models import Establecimiento

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

    def __unicode__(self):
        return unicode(self.tipo)