"""
    Definição dos modelos.
"""
from django.db import models

# Create your models here.


class Projeto(models.Model):
    """
    Modelo da persistência de Projetos
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    dt_criacao = models.DateField()
