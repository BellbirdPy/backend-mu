from django.contrib import admin
from models import *

# Register your models here.
class EstablecimientoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Establecimiento, EstablecimientoAdmin)
