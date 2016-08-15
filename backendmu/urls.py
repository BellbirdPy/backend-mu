"""backendmu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from compra.views import CompraViewSet, DetalleCompraViewSet
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from contabilidad.views import EgresoViewSet, ReporteEgresoViewSet, IngresoVarioViewSet, IngresoVentaViewSet, \
    TotalesViewSet
from establecimiento.views import EstablecimientoViewSet
from potrero.views import PotreroViewSet
from configuracion.views import CategoriaViewSet, RazaViewSet, PajuelaViewSet
from animal.views import AnimalViewSet
from lote.views import LoteViewSet,LoteAnimalCompletoViewSet
from mortandad.views import MortandadViewSet
from nutricion.views import NutricionViewSet
from sanitacion.views import *
from meteorologia.views import *
from empleado.views import *
from noticia.views import *
from django.conf import settings
from django.views.static import serve
from venta.views import VentaViewSet
from servicio.views import ServicioViewSet
from palpacion.views import PalpacionViewSet,PalpacionDetalleViewSet
from inseminacion.views import InseminacionViewSet,InseminacionDetalleViewSet

router = DefaultRouter()
router.register(r'noticia' ,NoticiaViewSet,base_name='noticia')
router.register(r'contratista' ,ContratistaViewSet,base_name='contratista')
router.register(r'empleado' ,EmpleadoViewSet,base_name='empleado')
router.register(r'meteorologia' ,RegistroViewSet,base_name='meteorologia')
router.register(r'potrero' ,PotreroViewSet,base_name='potrero')
router.register(r'establecimiento' ,EstablecimientoViewSet,base_name='establecimiento')
router.register(r'categoria' ,CategoriaViewSet,base_name='categoria')
router.register(r'raza' ,RazaViewSet,base_name='raza')
router.register(r'pajuela' ,PajuelaViewSet,base_name='pajuela')
router.register(r'animal' ,AnimalViewSet,base_name='animal')
router.register(r'lote_completo' ,LoteAnimalCompletoViewSet,base_name='lote_completo')
router.register(r'lote' ,LoteViewSet,base_name='lote')
router.register(r'mortandad' ,MortandadViewSet,base_name='mortandad')
router.register(r'nutricion' ,NutricionViewSet,base_name='nutricion')
router.register(r'compra',CompraViewSet,base_name='compra')
router.register(r'detalle_compra',DetalleCompraViewSet,base_name='detalle_compra')
router.register(r'sanitacion/eventos',EventoViewSet,base_name='sanitacion_eventos')
router.register(r'sanitacion/eventos_establecimiento',EventoEstablecimientoViewSet,base_name='sanitacion_eventos_establecimiento')
router.register(r'venta',VentaViewSet,base_name='venta')
router.register(r'servicio',ServicioViewSet,base_name='servicio')
router.register(r'sanitacion/vacunacion',VacunacionViewSet,base_name='vacunacion')
router.register(r'contabilidad/reporte_egreso',ReporteEgresoViewSet,base_name='reporte_egreso')
router.register(r'contabilidad/egreso',EgresoViewSet,base_name='egreso')
router.register(r'contabilidad/ingreso_vario',IngresoVarioViewSet,base_name='ingreso_vario')
router.register(r'contabilidad/ingreso_venta',IngresoVentaViewSet,base_name='ingreso_venta')
router.register(r'contabilidad/totales',TotalesViewSet,base_name='contabilidad_totales')

router.register(r'palpacion',PalpacionViewSet,base_name='palpacion')
router.register(r'palpacionDetalle',PalpacionDetalleViewSet,base_name='palpacion_detalle')
router.register(r'inseminacion',InseminacionViewSet,base_name='inseminacion')
router.register(r'inseminacionDetalle',InseminacionDetalleViewSet,base_name='inseminacion_detalle')






urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^password/', include('password_reset.urls')),
    url(r'^', include('home.urls')),
    url(r'^establecimiento/', include('establecimiento.urls')),
    url(r'^animal/', include('animal.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
]

if settings.DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))

