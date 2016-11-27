from django.contrib import admin
from models import *

# Register your models here.
class EstablecimientoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','last_login')

admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Establecimiento, EstablecimientoAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

