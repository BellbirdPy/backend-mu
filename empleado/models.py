# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from establecimiento.models import Establecimiento

from django.db import models

'''Registro de Empleados:
Datos Obligatorios: Nombre, Apellido, Número de Cédula, Nacimiento, Dirección, Teléfono. Ingreso a la Empresa, Cargo, Salario.
Datos Opcionales: Ciudad de Nacimiento, Contacto de Emergencia, Mail, Escaneo de la Cédula de Identidad (JPEG).
Registro de Contratista:
Datos Obligatorios: Nombre, Apellido, Número de Cédula, Teléfono, Nacimiento, Actividad, Jornal. '''
# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero_cedula = models.CharField(max_length=12)
    fecha_nacimiento = models.DateTimeField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ingreso_empresa = models.DateTimeField()
    cargo = models.CharField(max_length=40)
    salario = models.IntegerField()
    ciudad_nacimiento = models.CharField(max_length=30, blank=True, null=True)
    contacto_emergencia = models.TextField(blank=True,null=True)
    mail = models.EmailField(blank=True,null=True)
    escaneo_cedula = models.ImageField(blank=True,null=True)
    establecimiento = models.ForeignKey(Establecimiento,related_name='empleados')



    def __unicode__(self):
        return unicode(self.apellido) + ', ' + unicode(self.nombre)

class Contratista(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero_cedula = models.CharField(max_length=12,null=True,blank=True)
    fecha_nacimiento = models.DateTimeField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    actividad = models.CharField(max_length=40)
    jornal = models.IntegerField()
    establecimiento = models.ForeignKey(Establecimiento,related_name='contratistas')



    def __unicode__(self):
        return unicode(self.apellido) + ', ' + unicode(self.nombre)