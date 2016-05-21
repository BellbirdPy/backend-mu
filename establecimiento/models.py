from __future__ import unicode_literals
from django.utils.timezone import now

import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import date



# Create your models here.
class Establecimiento(models.Model):
    CHOICES_ESTADO = (
        ("A", "Activo"),
        ("E", "Expirado"),
        ("B","Borrado")
    )
    nombre = models.CharField(max_length=100)
    owner = models.ForeignKey(User,related_name='establecimientos_owner')
    miembros = models.ManyToManyField(User,related_name='establecimientos',blank=True)
    estado = models.CharField(max_length=1, choices=CHOICES_ESTADO, default="A")
    fecha_expiracion = models.DateField()

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


