from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    is_hembra = models.BooleanField()

    def __unicode__(self):
        return unicode(self.nombre)



class Raza(models.Model):
    nombre = models.CharField(max_length=80)

    def __unicode__(self):
        return unicode(self.nombre)