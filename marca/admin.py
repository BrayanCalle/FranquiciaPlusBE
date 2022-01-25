from django.contrib import admin

from marca.models import Marca, Categoria, Ubicacion, Directorio, Estado


class MarcaAdmin(admin.ModelAdmin):
    """Administración de Marca"""
    list_display = ("nombre", "precio", "categoria", "estado")
    search_fields = ("nombre", "descripcion", "estado")
    list_filter = ("nombre", "categoria", "estado")




admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria)
admin.site.register(Ubicacion)
admin.site.register(Directorio)
admin.site.register(Estado)
