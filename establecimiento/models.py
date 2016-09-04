from __future__ import unicode_literals

from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.nombre)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, related_name='ciudad')

    def __unicode__(self):
        return unicode(self.nombre)


# Create your models here.
class Establecimiento(models.Model):
    CHOICES_ESTADO = (
        ("A", "Activo"),
        ("E", "Expirado"),
        ("B", "Borrado")
    )
    CHOICES_PLAN = (
        ("P", "Premium"),
        ("E", "Estandar"),
        ("G", "Educativo"),
    )

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, related_name='establecimiento', null=True, default=True)
    ciudad = models.CharField(max_length=30, null=True, blank=True)
    owner = models.ForeignKey(User, related_name='establecimientos_owner')
    miembros = models.ManyToManyField(User, related_name='establecimientos', blank=True)
    estado = models.CharField(max_length=1, choices=CHOICES_ESTADO, default="A")
    plan = models.CharField(max_length=1, choices=CHOICES_PLAN, default="G")
    fecha_expiracion = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.nombre)

    @property
    def is_expired(self):
        if date.today() > self.fecha_expiracion:
            return True
        return False

    @property
    def dias_restantes(self):
        resto = self.fecha_expiracion - date.today()
        return resto.days

    def user_can_manage_me(self, user):
        return user == self.owner


class Tarea(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50, default='')
    leido = models.BooleanField(default=False)
    usuario_asignado = models.ForeignKey(User, related_name='tarea_asignada')
    usuario_creador = models.ForeignKey(User, related_name='tarea_creada', null=True)
    establecimiento = models.ForeignKey(Establecimiento, related_name='tarea')

    def __unicode__(self):
        return unicode(self.fecha) + ', ' + unicode(self.descripcion)

    def get_usuario_asignado_display(self):
        return self.usuario_asignado.username
