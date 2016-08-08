from __future__ import unicode_literals

from django.db import models

from animal.models import Animal
from configuracion.models import Raza, Categoria
from lote.models import Lote

porcentaje = (('25', 25), ('50', 50), ('75', 75), ('100', 100))
t_servicio = (('Monta Natural', 'MN'), ('Inceminacion Artificial', 'IA'))
car = (('0',0),('1',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9))

class LoteGenetica(models.Model):
    lote = models.OneToOneField(Lote)
    raza = models.ForeignKey(Raza)
    categoria = models.ForeignKey(Categoria)
    porcentaje_pureza = models.PositiveIntegerField(choices=porcentaje)

    tipo_servicio = models.CharField(max_length=2, choices=t_servicio)
    carimbo = models.PositiveIntegerField(choices=car)
    descripcion = models.TextField()
    pedigree_padre = models.CharField(max_length=32)


class AnimalGenetica(models.Model):
    animal = models.OneToOneField(Animal)
    nombre = models.CharField(max_length=128)
    nombre_corto = models.CharField(max_length=32)
    porcentaje = (('25', 25), ('50', 50), ('75', 75), ('100', 100))
    porcentaje_pureza = models.PositiveIntegerField(choices=porcentaje)
    tipo_servicio = models.CharField(max_length=2, choices=t_servicio)
    rp = models.CharField(max_length=32)
    descripcion = models.TextField()
    cantidad_pajuelas = models.PositiveIntegerField()
    pedigree_padre = models.CharField(max_length=32)
    pedigree_madre = models.CharField(max_length=32)
    pedigree_abuelo = models.CharField(max_length=32)
