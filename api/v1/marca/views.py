from rest_framework import viewsets
from marca.models import Directorio, Estado, Inversion, Marca, Categoria, Ubicacion
from api.v1.marca.serializers import DirectorioSerializer, EstadoSerializer, MarcaSerializer, CategoriaSerializer, UbicacionSerializer, InversionSerializer
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
        'estado__nombre': ['exact'],
        'ubicacion__nombre': ['exact'],
        'directorio__nombre': ['exact'],
        'inversion': ['exact'],
    }
    queryset = Marca.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializer
    filter_backends = [OrderingFilter]
    ordering = ["nombre"]
    queryset = Categoria.objects.all()

class UbicacionViewSet(viewsets.ModelViewSet):
    serializer_class= UbicacionSerializer
    filter_backends = [OrderingFilter]
    ordering = ["nombre"]
    queryset = Ubicacion.objects.all()

class InversionViewSet(viewsets.ModelViewSet):
    serializer_class= InversionSerializer
    filter_backends = [OrderingFilter]
    ordering = ["id"]
    queryset = Inversion.objects.all()
    
class EstadoViewSet(viewsets.ModelViewSet):
    serializer_class= EstadoSerializer
    filter_backends = [OrderingFilter]
    ordering = ["nombre"]
    queryset = Estado.objects.all()

class DirectorioViewSet(viewsets.ModelViewSet):
    serializer_class= DirectorioSerializer
    filter_backends = [OrderingFilter]
    ordering = ["nombre"]
    queryset = Directorio.objects.all()