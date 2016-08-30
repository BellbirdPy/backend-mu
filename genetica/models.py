from __future__ import unicode_literals

from django.db import models

from animal.models import Animal, Establecimiento
from configuracion.models import Raza, Categoria
from lote.models import Lote

porcentaje = ((25, 25), (50, 50), (75, 75), (100, 100))
t_servicio = (('MN', 'Monta Natural'), ('IA', 'Inceminacion Artificial'))
car = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9))


class LoteGenetica(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, related_name="lote_genetica")
    lote = models.OneToOneField(Lote)
    raza = models.ForeignKey(Raza)
    categoria = models.ForeignKey(Categoria)
    porcentaje_pureza = models.PositiveIntegerField(choices=porcentaje)

    tipo_servicio = models.CharField(max_length=2, choices=t_servicio)
    carimbo = models.PositiveIntegerField(choices=car)
    descripcion = models.TextField()
    pedigree_padre = models.CharField(max_length=32)


class AnimalGenetica(models.Model):
    lote_genetica = models.ForeignKey(LoteGenetica, related_name="animal_genetica", null=True, blank=True,
                                      on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, related_name="animal_genetica")
    animal = models.OneToOneField(Animal)
    nombre = models.CharField(max_length=128, null=True, blank=True)
    nombre_corto = models.CharField(max_length=32, null=True, blank=True)
    porcentaje_pureza = models.PositiveIntegerField(choices=porcentaje)
    tipo_servicio = models.CharField(max_length=2, choices=t_servicio)
    rp = models.CharField(max_length=32, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    cantidad_pajuelas = models.PositiveIntegerField(default=0, null=True, blank=True)
    pedigree_padre = models.CharField(max_length=32, null=True, blank=True)
    pedigree_madre = models.CharField(max_length=32, null=True, blank=True)
    pedigree_abuelo = models.CharField(max_length=32, null=True, blank=True)
