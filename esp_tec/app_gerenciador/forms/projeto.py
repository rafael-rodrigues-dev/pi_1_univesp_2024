"""
Form do Projeto
"""
from django import forms
from app_gerenciador.models import Projeto


class ProjetoForm(forms.ModelForm):
    """
    Declara o form do Projeto
    """
    
    class Meta:
        """
        Define os campos que compõem o form
        """
        model = Projeto

        fields = [
            'nome',
            'dt_criacao',
            'descricao',
            'lista_de_materiais'
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'dt_criacao': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'cols': 20
                }
            ),
            'lista_de_materiais': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }

        labels = {
            'nome': 'Nome',
            'dt_criacao': 'Data de criação',
            'lista_de_materiais': 'Lista de Materiais'
        }
