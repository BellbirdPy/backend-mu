
from rest_framework import viewsets, filters
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.

class VentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('fecha_venta',)

    def create(self, request, *args, **kwargs):
        return super(VentaViewSet, self).create(request,*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            for lote in instance.lotes.all():
                lote.estado = 'N'
                lote.save()
            for animal in instance.animales.all():
                animal.estado = 'V'
                animal.save()
            self.perform_destroy(instance)
        except:
            pass
        return super(VentaViewSet, self).destroy(request,*args,**kwargs)
