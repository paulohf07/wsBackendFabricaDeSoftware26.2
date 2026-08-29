from django.contrib import admin

# Register your models here.
from .models import Entregador, Moto, HistoricoConsulta

admin.site.register(Entregador)
admin.site.register(Moto)
admin.site.register(HistoricoConsulta)