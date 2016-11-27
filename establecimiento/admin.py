from django.contrib import admin
from models import *

# Register your models here.
class EstablecimientoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)
    list_display = ('nombre','fecha_creacion','get_owner','get_owner_mail')

    def get_owner(self, obj):
        return obj.owner.first_name + ' ' + obj.owner.last_name
    get_owner.short_description = 'Dueno'

    def get_owner_mail(self, obj):
        return obj.owner.email

    get_owner.short_description = 'Dueno email'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','last_login')

admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Establecimiento, EstablecimientoAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

