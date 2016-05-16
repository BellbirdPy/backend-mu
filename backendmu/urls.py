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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from establecimiento.views import EstablecimientoViewSet
from potrero.views import PotreroViewSet
from configuracion.views import CategoriaViewSet, RazaViewSet
from animal.views import AnimalViewSet
from lote.views import LoteViewSet

router = DefaultRouter()
router.register(r'potrero' ,PotreroViewSet,base_name='potrero')
router.register(r'establecimiento' ,EstablecimientoViewSet,base_name='establecimiento')
router.register(r'categoria' ,CategoriaViewSet,base_name='categoria')
router.register(r'raza' ,RazaViewSet,base_name='raza')
router.register(r'animal' ,AnimalViewSet,base_name='animal')
router.register(r'lote' ,LoteViewSet,base_name='lote')



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
]
