from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    owner = models.ForeignKey(User,related_name='establecimientos_owner')
    miembros = models.ManyToManyField(User,related_name='establecimientos',blank=True)

    def __unicode__(self):
        return unicode(self.nombre)
