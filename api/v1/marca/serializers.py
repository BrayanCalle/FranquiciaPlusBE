from rest_framework import serializers
from marca.models import Marca

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        read_only_fields = [
            "id",
        ]
        fields = [
            "nombre", "precio", "descripcion",
            "imagenmarca", "imagenlocal", "imagenlogo"
        ] + read_only_fields
        
        