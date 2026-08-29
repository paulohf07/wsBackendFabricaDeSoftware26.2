from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Categoria')
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Produto')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos', verbose_name='Categoria')

    def __str__(self):
        return f"{self.nome} - R${self.preco}"