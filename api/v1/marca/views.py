from rest_framework import viewsets
from marca.models import Marca
from api.v1.marca.serializers import MarcaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class= MarcaSerializer
    queryset = Marca.objects.all()
    