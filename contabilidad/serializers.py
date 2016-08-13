from rest_framework import serializers
from models import *

class EgresoSerializer(serializers.ModelSerializer):
    rubro_display = serializers.CharField(source='get_rubro_display', read_only=True)
    class Meta:
        model = Egreso
        fields = ('id','fecha','descripcion', 'rubro', 'monto','establecimiento', 'rubro_display')

"""
    def create(self, validated_data):

        print validated_data
        egreso = Egreso.objects.create(**validated_data)
        rubro, created = ReporteEgreso.objects.get_or_create(establecimiento=egreso.establecimiento,mes=egreso.fecha.month,
                                                    anho=egreso.fecha.year)
        if egreso.rubro == 'GD':
            rubro.gastos_directos += egreso.monto
            rubro.save()
            descripcion, created = ReporteDescripcion.objects.get_or_create(rubro=rubro, nombre=egreso.descripcion)
            descripcion.monto_des += egreso.monto
            descripcion.save()
            for d in ReporteDescripcion.objects.filter(rubro=rubro).values('nombre').distinct():
                d.porcentaje = (d.monto_des/rubro.gastos_directos)*100
                d.save()

        if egreso.rubro == 'GA':
            rubro.gastos_administrativos += egreso.monto
            rubro.save()
            descripcion, created = ReporteDescripcion.objects.get_or_create(rubro=rubro, nombre=egreso.descripcion)
            descripcion.monto_des += egreso.monto
            descripcion.save()
            for d in ReporteDescripcion.objects.filter(rubro=rubro).values('nombre').distinct():
                d.porcentaje = (d.monto_des / rubro.gastos_administrativos) * 100
                d.save()
        if egreso.rubro == 'IT':
            rubro.impuestos += egreso.monto
            rubro.save()
            descripcion, created = ReporteDescripcion.objects.get_or_create(rubro=rubro, nombre=egreso.descripcion)
            descripcion.monto_des += egreso.monto
            descripcion.save()
            for d in ReporteDescripcion.objects.filter(rubro=rubro).values('nombre').distinct():
                d.porcentaje = (d.monto_des / rubro.impuestos) * 100
                d.save()
        if egreso.rubro == 'GC':
            rubro.gastos_comercializacion += egreso.monto
            rubro.save()
            descripcion, created = ReporteDescripcion.objects.get_or_create(rubro=rubro, nombre=egreso.descripcion)
            descripcion.monto_des += egreso.monto
            descripcion.save()
            for d in ReporteDescripcion.objects.filter(rubro=rubro).values('nombre').distinct():
                d.porcentaje = (d.monto_des / rubro.gastos_comercializacion) * 100
                d.save()

        if egreso.rubro == 'GF':
            rubro.gastos_financieros += egreso.monto
            rubro.save()
            descripcion, created = ReporteDescripcion.objects.get_or_create(rubro=rubro, nombre=egreso.descripcion)
        descripcion.monto_des += egreso.monto
            descripcion.save()
            for d in ReporteDescripcion.objects.filter(rubro=rubro).values('nombre').distinct():
                d.porcentaje = (d.monto_des / rubro.gastos_financieros) * 100
                d.save()


        return egreso
"""""


class IngresoVarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngresoVario
        fields = ('id','fecha','motivo', 'comprador', 'cantidad','establecimiento', 'precio_unitario')