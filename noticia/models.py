from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to='images/',default='')
    texto = RichTextField()
    fecha = models.DateField(db_index=True, auto_now_add=True)
    activo = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.titulo)
