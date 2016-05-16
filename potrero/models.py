from __future__ import unicode_literals

from django.db import models
from establecimiento.models import Establecimiento

# Create your models here.
class Potrero(models.Model):
    nombre = models.CharField(max_length=100)
    superficie = models.IntegerField(blank=True)
    uso = models.TextField()
    establecimiento = models.ForeignKey(Establecimiento,related_name='potreros')

    def __unicode__(self):
        return unicode(self.nombre)