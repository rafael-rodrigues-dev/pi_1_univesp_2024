"""
    Definição dos modelos.
"""
from django.db import models

# Create your models here.


class Material(models.Model):
    """
    Modelo da persistência de Materiais
    """

    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do material'
    )

    unidade_medida = models.CharField(
        max_length=15,
        verbose_name='Unidade de medida'
    )

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Materiais"

    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.nome)


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

    lista_de_materiais = models.ManyToManyField(
        Material,
        verbose_name='Lista de materiais'
    )

    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.nome)

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Projetos"
        
class Servico(models.Model):
    """
    Modelo da persistência de Serviços
    """
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do serviço'
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    dt_inicio = models.DateField(
        verbose_name='Data de inicio'
    )

    dt_entrega = models.DateField(
        verbose_name='Data de entrega'
    )
    
    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.nome)

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Serviços"