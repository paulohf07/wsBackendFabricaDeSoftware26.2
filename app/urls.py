from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import EntregadorViewSet, MotoViewSet, HistoricoConsultaViewSet, ConsultaEntregaViewSet

router = DefaultRouter()
router.register(r'entregadores', EntregadorViewSet)
router.register(r'motos', MotoViewSet)
router.register(r'historico', HistoricoConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('consultar-entrega/', ConsultaEntregaViewSet.as_view(), name='consultar-entrega'),
]