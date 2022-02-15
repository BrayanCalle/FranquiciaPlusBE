from django.contrib import admin

from marca.models import Marca, Categoria, Ubicacion, Directorio, Estado, Inversion, Prioridad


class MarcaAdmin(admin.ModelAdmin):
    """Administración de Marca"""
    list_display = ("nombre", "estado", "precio","inversion")
    search_fields = ("nombre", "ubicacion", "descripcion", "estado")
    list_filter = ("estado", "categoria", "ubicacion")

class CategoriaAdmin(admin.ModelAdmin):
    """Administración de Categoria"""
    search_fields = ("nombre",)

class UbicacionAdmin(admin.ModelAdmin):
    """Administración de Ubicacion"""
    search_fields = ("nombre",)



admin.site.site_header = 'Administración Franquicia Plus'
admin.site.index_title = 'Panel de Control Franquicia Plus'
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Directorio)
admin.site.register(Estado)
admin.site.register(Inversion)
admin.site.register(Prioridad)
