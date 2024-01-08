from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    valor_minimo = models.DecimalField(max_digits=5, decimal_places=2)
    qtd_horas = models.IntegerField(null=False, blank=False)
    porcentagem_comissao = models.FloatField(null=False, blank=False)