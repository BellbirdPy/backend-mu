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


class TotalesViewSet (viewsets.ViewSet):
    def list(self, request, format=None):
        if (request.query_params):
            total_ingresos_venta = 0
            total_ingresos_varios = 0
            total_cantidad_venta = 0
            establecimiento = request.query_params.get('establecimiento')
            for ingreso_venta in IngresoVenta.objects.filter(establecimiento=establecimiento):
                total_cantidad_venta = total_cantidad_venta+ingreso_venta.cantidad
                total_ingresos_venta = total_ingresos_venta+ingreso_venta.total
            for ingreso_vario in IngresoVario.objects.filter(establecimiento=establecimiento):
                total_ingresos_varios = total_ingresos_varios+(ingreso_vario.precio_unitario*ingreso_vario.cantidad)
            response = {'total_ingresos_venta': total_ingresos_venta,'total_ingresos_varios': total_ingresos_varios,'total_cantidad_venta': total_cantidad_venta}
        else:
            response = {'total_ingresos_venta': 0,'total_ingresos_varios': 0,'total_cantidad_venta': 0}
        return Response(response)



class EgresoViewSet(viewsets.ModelViewSet):
    serializer_class = EgresoSerializer
    queryset = Egreso.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento','rubro',)
    ordering_fields = '__all__'
    ordering = ('fecha',)


class IngresoVarioViewSet(viewsets.ModelViewSet):
    serializer_class = IngresoVarioSerializer
    queryset = IngresoVario.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('fecha',)


class IngresoVentaViewSet(viewsets.ModelViewSet):
    serializer_class = IngresoVentaSerializer
    queryset = IngresoVenta.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('fecha',)