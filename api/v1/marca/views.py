from rest_framework import viewsets
from marca.models import Inversion, Marca, Categoria, Ubicacion
from api.v1.marca.serializers import MarcaSerializer, CategoriaSerializer, UbicacionSerializer, InversionSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from pagination import MarcaPagination

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class= MarcaSerializer
    pagination_class = MarcaPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
    ordering_fields = ["prioridad","created_at", "nombre", "precio"]
    ordering = ["prioridad","-created_at"]
    search_fields = ["nombre", "categoria__nombre", "precio"]
    filterset_fields = {
        'precio': ['gte','lte'],
        'categoria__nombre': ['exact'],
        'estado': ['exact'],
        'ubicacion__nombre': ['exact'],
        'directorio': ['exact'],
        'inversion__nombre': ['exact'],
    }
    queryset = Marca.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializer
    queryset = Categoria.objects.all()

class UbicacionViewSet(viewsets.ModelViewSet):
    serializer_class= UbicacionSerializer
    queryset = Ubicacion.objects.all()

class InversionViewSet(viewsets.ModelViewSet):
    serializer_class= InversionSerializer
    queryset = Inversion.objects.all()
    