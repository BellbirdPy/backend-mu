from __future__ import unicode_literals
from establecimiento.models import *
from django.db import models

# Create your models here.
class Mortandad(models.Model):
    CHOICES_TIPO = (
        ("M","Mortandad"),
        ("A","Abigeo")
    )
    tipo = models.CharField(max_length=1,choices=CHOICES_TIPO,default='M')
    fecha = models.DateTimeField()
    razon = models.TextField()
    establecimiento = models.ForeignKey(Establecimiento,related_name='mortandades')

    def __unicode__(self):
        return unicode(self.fecha) + ' - ' + unicode(self.razon)
