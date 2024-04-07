from django.contrib import admin

# Register your models here.

from django.utils.html import format_html
from django.urls import reverse_lazy

from .models import Projeto, Material, Servico

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    """ Classe admin para o Projeto """
    list_display = ("nome", "dt_criacao", "pdf_url")

    def get_ordering(self, request):
        return ['nome', ]
    
    def pdf_url(self, obj):
        """ Cria a link do pdf para ser exibido na coluna da listagem """
        url =  reverse_lazy('report_pdf', kwargs={'pk': obj.id})
        return format_html(f"<a target='_blank' href='{url}'>PDF</a>")
    
    pdf_url.allow_tags = True
    pdf_url.short_description = 'Especificação Técnica'


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    """ Classe admin para o Material """
    list_display = ("nome", "unidade_medida")

    def get_ordering(self, request):
        return ['nome', ]

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    """ Classe admin para o Serviço """
    list_display = ("codigo", "nome", "descricao", "unidade_medida", "quantidade")

    def get_ordering(self, request):
        return ['nome', ]


