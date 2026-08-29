from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import CategoriaViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]