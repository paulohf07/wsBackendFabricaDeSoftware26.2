from django.db import models

# Create your models here.

class Entregador(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome
    
class Moto(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE, related_name='motos')

    def __str__(self):
        return f"{self.modelo} ({self.placa})"
    
class HistoricoConsulta(models.Model):
    cep = models.CharField(max_length=10)
    state = models.CharField(max_length=2, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    temperatura = models.FloatField(null=True, blank=True)
    data_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.cep} ({self.data_consulta.strftime('%d/%m/%Y %H:%M')})"