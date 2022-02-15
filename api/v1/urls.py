from django.urls import path
from rest_framework import routers
from api.v1.marca.views import InversionViewSet, MarcaViewSet, CategoriaViewSet, UbicacionViewSet

router = routers.SimpleRouter()
router.register(r'marcas', MarcaViewSet, basename="marcas")
router.register(r'categoria', CategoriaViewSet, basename="categoria")
router.register(r'ubicacion', UbicacionViewSet, basename="ubicacion")
router.register(r'inversion', InversionViewSet, basename="inversion")

urlpatterns = router.urls