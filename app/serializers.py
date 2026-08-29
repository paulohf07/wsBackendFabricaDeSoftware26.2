from rest_framework import serializers
from app.models import Entregador, Moto, HistoricoConsulta

class EntregadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entregador
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'

class HistoricoConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoConsulta
        fields = '__all__'
