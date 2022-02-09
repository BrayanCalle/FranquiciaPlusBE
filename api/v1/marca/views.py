from rest_framework import viewsets
from marca.models import Marca, Categoria, Ubicacion
from api.v1.marca.serializers import MarcaSerializer, CategoriaSerializer, UbicacionSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from pagination import MarcaPagination

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class= MarcaSerializer
    pagination_class = MarcaPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
    ordering_fields = ["created_at", "nombre", "precio"]
    ordering = ["-created_at"]
    search_fields = ["nombre", "categoria__id", "precio"]
    filterset_fields = {
        'precio': ['gte','lte'],
        'categoria': ['exact'],
        'estado': ['exact'],
        'ubicacion': ['exact'],
        'directorio': ['exact'],
    }
    queryset = Marca.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializer
    queryset = Categoria.objects.all()

class UbicacionViewSet(viewsets.ModelViewSet):
    serializer_class= UbicacionSerializer
    queryset = Ubicacion.objects.all()
    