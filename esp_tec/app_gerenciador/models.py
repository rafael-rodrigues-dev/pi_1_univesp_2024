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

class Servico(models.Model):
    """
    Modelo da persistência de Serviços
    """
    
    codigo = models.CharField(
        max_length=100,
        verbose_name='Codigo do serviço',
        null=True     
    )
    
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do serviço'
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    unidade_medida = models.CharField(
        max_length=15,
        verbose_name='Unidade de medida',
        null=True
    )

    quantidade = models.CharField(
        max_length=15,
        verbose_name='Quantidade',
        null=True
    )

    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.codigo)

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Serviços"

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
    lista_de_servicos = models.ManyToManyField(
        Servico,
        verbose_name='Lista de codigo de serviços',
        
    )
    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.nome)

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Projetos"
        