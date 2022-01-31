from django.urls import path
from rest_framework import routers
from api.v1.marca.views import MarcaViewSet

router = routers.SimpleRouter()
router.register('marcas', MarcaViewSet)

urlpatterns = router.urls