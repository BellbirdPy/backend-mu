
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from serializers import *
from models import *
from scripts.related_ordering import RelatedOrderingFilter
# Create your views here.

class ParicionViewSet(viewsets.ModelViewSet):
    serializer_class = ParicionSerializer
    queryset = Paricion.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,RelatedOrderingFilter)
    filter_fields = ('establecimiento',)
    ordering_fields = '__all__'
    ordering = ('-fecha',)

    def create(self, request, *args, **kwargs):
        if 'pariciones' in request.data:
            pariciones = request.data['pariciones']
            print pariciones
            serializer = self.get_serializer(data=pariciones, many=True)

            if serializer.is_valid():
                print 'valid'
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED,
                                headers=headers)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super(ParicionViewSet, self).create(request, *args, **kwargs)