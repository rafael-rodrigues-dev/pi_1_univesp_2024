"""
    Definição dos modelos.
"""
from django.db import models

# Create your models here.


class Projeto(models.Model):
    """
    Modelo da persistência de Projetos
    """
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do projeto'
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    dt_criacao = models.DateField(
        verbose_name='Data de criação'
    )

    def __str__(self):
        return str(self.nome)
