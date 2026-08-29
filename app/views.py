from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from app.models import Categoria, Produto
from app.api.serializers import CategoriaSerializer, ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer    