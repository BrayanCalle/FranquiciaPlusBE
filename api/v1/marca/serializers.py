from rest_framework import serializers
from marca.models import Marca, Categoria, Ubicacion

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        read_only_fields = [
            "id",
        ]
        fields = [
            "created_at","nombre", "precio", "descripcion",
            "imagenmarca", "imagenlocal", "imagenlogo",
            "categoria","estado","ubicacion","directorio"
        ] + read_only_fields
        depth=1

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        read_only_fields = [
            "id",
        ]
        fields = [
            "nombre",
        ] + read_only_fields

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        read_only_fields = [
            "id",
        ]
        fields = [
            "nombre",
        ] + read_only_fields