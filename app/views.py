from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Entregador, Moto, HistoricoConsulta
from app.serializers import EntregadorSerializer, MotoSerializer, HistoricoConsultaSerializer
from app.services import consultar_cep_e_clima

class EntregadorViewSet(viewsets.ModelViewSet):
    queryset = Entregador.objects.all()
    serializer_class = EntregadorSerializer

class MotoViewSet(viewsets.ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

class HistoricoConsultaViewSet(viewsets.ModelViewSet):
    queryset = HistoricoConsulta.objects.all().order_by('-data_consulta')
    serializer_class = HistoricoConsultaSerializer

class ConsultaEntregaViewSet(APIView):
    def get(self, request):
        cep = request.GET.get('cep')
        if not cep:
            return Response({"erro": "O parâmetro 'cep' é obrigatório."}, status=400)
        
        resultado, status_code = consultar_cep_e_clima(cep)
        return Response(resultado, status=status_code)
        