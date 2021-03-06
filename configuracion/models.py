from __future__ import unicode_literals
from establecimiento.models import Establecimiento
from django.db import models

# Create your models here.
class Categoria(models.Model):
    codigo = models.CharField(max_length=20, default='')
    nombre = models.CharField(max_length=80)
    is_hembra = models.BooleanField()
    establecimiento = models.ForeignKey(Establecimiento,related_name='categorias',null=True,default=None,blank=True)
    fecha_creacion = models.DateTimeField(auto_now=True)



    def __unicode__(self):
        return unicode(self.nombre)



class Raza(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True,default="")
    establecimiento = models.ForeignKey(Establecimiento,related_name='razas',null=True,default=None,blank=True)
    fecha_creacion = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return unicode(self.nombre)

class Pajuela(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True,default="")
    establecimiento = models.ForeignKey(Establecimiento,related_name='pajuelas')
    fecha_creacion = models.DateTimeField(auto_now=True)



    def __unicode__(self):
        return unicode(self.nombre)