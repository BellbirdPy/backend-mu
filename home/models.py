from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=100)


# User
def user_post_save(sender, instance, signal, *args, **kwargs):
    # Creates user profile
    profile, new = UserProfile.objects.get_or_create(usuario=instance)


post_save.connect(user_post_save, sender=User)
