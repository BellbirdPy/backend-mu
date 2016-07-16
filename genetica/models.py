from __future__ import unicode_literals

from animal.models import Animal
from configuracion.models import Raza, Categoria
from django.db import models

# Create your models here.
from lote.models import Lote


class LoteGenetica(models.Model):
    lote = models.OneToOneField(Lote)
    raza = models.ForeignKey(Raza)
    categoria = models.ForeignKey(Categoria)
    porcentaje_pureza = models.PositiveIntegerField(choices=[25, 50, 75, 100])
    tipo_servicio = models.CharField(choices={['Monta Natural','MN'],['Inceminacion Artificial','IA']})
    carimbo = models.PositiveIntegerField(choices=[0,1,2,3,4,5,6,7,8,9])
    descripcion = models.TextField()
    pedigree_padre = models.CharField(max_length=32)

class AnimalGenetica(models.Model):
    animal = models.OneToOneField(Animal)
    nombre = models.CharField(max_length=128)
    nombre_corto = models.CharField(max_length=32)
    porcentaje_pureza = models.PositiveIntegerField(choices=[25, 50, 75, 100])
    tipo_servicio = models.CharField(choices={['Monta Natural', 'MN'], ['Inceminacion Artificial', 'IA']})
    rp = models.CharField(max_length=32)
    descripcion = models.TextField()
    cantidad_pajuelas = models.PositiveIntegerField()
    pedigree_padre = models.CharField(max_length=32)
    pedigree_madre = models.CharField(max_length=32)
    pedigree_abuelo = models.CharField(max_length=32)

