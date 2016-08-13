#encoding:utf-8
from __future__ import division
from rest_framework import viewsets,filters
from rest_framework.views import Response
from serializers import *
from models import *
# Create your views here.
class ReporteEgresoViewSet (viewsets.ViewSet):
    def list(self, request, format=None):
        if (request.query_params):
            mes = request.query_params.get('mes')
            anho = request.query_params.get('anho')
            establecimiento = request.query_params.get('establecimiento')
            reportes = []
            request.mes=8
            request.anho=2016
            rubros = [{'c':'GD','n':'Gastos Directos'}, {'c':'GA','n':'Gastos Administrativos'}, {'c':'IT','n':'Impuestos y Tazas'},
                      {'c':'GC', 'n':'Gastos de Comercializacion'}, {'c':'GF','n':'Gastos Financieros'}]
            total_reporte = 0
            for rubro in rubros:
                descripciones = []
                total_rubro = 0
                for egreso in Egreso.objects.filter(establecimiento=establecimiento, rubro=rubro['c'], fecha__month=mes, fecha__year=anho)\
                        .values('descripcion').distinct():
                    total = 0
                    for descripcion in Egreso.objects.filter(establecimiento=establecimiento,rubro=rubro['c'], descripcion=egreso['descripcion'],
                                                             fecha__month=mes, fecha__year=anho)\
                            .values('monto'):
                        total = total + descripcion['monto']
                    descripciones.append({'nombre': egreso['descripcion'], 'monto': total, 'porcentaje': 0.0})
                    total_rubro = total_rubro + total
                    for des in descripciones:
                        print des['monto']/total_rubro
                        des['porcentaje'] = round((des['monto']/total_rubro)*100, 2)
                reportes.append({'rubro': rubro['n'], 'monto_rubro': total_rubro, 'descripciones': descripciones})
                total_reporte = total_reporte + total_rubro
            response = {'count': len(reportes), 'next': None, 'previous': None, 'results': reportes, 'total_reporte': total_reporte}
        else:
            response = {'count': 0, 'next': None, 'previous': None, 'results': None, 'total_reporte': None}
        return Response(response)

class EgresoViewSet(viewsets.ModelViewSet):
    serializer_class = EgresoSerializer
    queryset = Egreso.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento','monto',)
    ordering_fields = '__all__'
    ordering = ('fecha',)
    """
    def create(self, request, *args, **kwargs):
        return super(EgresoViewSet, self).create(request,*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            egreso = self.get_object()
            try:
                rubro, created = ReporteEgreso.objects.get(establecimiento=egreso.establecimiento,
                                                            mes=egreso.fecha.month, anho=egreso.fecha.year)
                if egreso.rubro == 'GD':
                    rubro.gastos_directos -= egreso.monto
                    rubro.save()
                    descripcion, created = ReporteDescripcion.objects.get(rubro=rubro, nombre=egreso.descripcion)
                    descripcion.monto_des -= egreso.monto
                    descripcion.porcentaje = (descripcion.monto_des / rubro.gastos_directos)*100
                    descripcion.save()
                if egreso.rubro == 'GA':
                    rubro.gastos_administrativos += egreso.monto
                    rubro.save()
                    descripcion, created = ReporteDescripcion.objects.get(rubro=rubro, nombre=egreso.descripcion)
                    descripcion.monto_des -= egreso.monto
                    descripcion.porcentaje = (descripcion.monto_des / rubro.gastos_administrativos)*100
                    descripcion.save()
                if egreso.rubro == 'IT':
                    rubro.impuestos -= egreso.monto
                    rubro.save()
                    descripcion, created = ReporteDescripcion.objects.get(rubro=rubro, nombre=egreso.descripcion)
                    descripcion.monto_des -= egreso.monto
                    descripcion.porcentaje = (descripcion.monto_des / rubro.impuestos)*100
                    descripcion.save()
                if egreso.rubro == 'GC':
                    rubro.gastos_comercializacion -= egreso.monto
                    rubro.save()
                    descripcion, created = ReporteDescripcion.objects.get(rubro=rubro, nombre=egreso.descripcion)
                    descripcion.monto_des -= egreso.monto
                    descripcion.porcentaje = (descripcion.monto_des / rubro.gastos_comercializacion)*100
                    descripcion.save()
                if egreso.rubro == 'GF':
                    rubro.gastos_financieros -= egreso.monto
                    rubro.save()
                    descripcion, created = ReporteDescripcion.objects.get(rubro=rubro, nombre=egreso.descripcion)
                    descripcion.monto_des -= egreso.monto
                    descripcion.porcentaje = (descripcion.monto_des / rubro.gastos_financieros)*100
                    descripcion.save()
                self.perform_destroy(egreso)
            except ReporteDescripcion.DoesNotExist or ReporteEgreso.DoesNotExist:
                pass
        except:
            pass
        return super(EgresoViewSet, self).destroy(request,*args,**kwargs) """""

class IngresoVarioViewSet(viewsets.ModelViewSet):
    serializer_class = IngresoVarioSerializer
    queryset = IngresoVario.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento','fecha',)
    ordering_fields = '__all__'
    ordering = ('fecha',)