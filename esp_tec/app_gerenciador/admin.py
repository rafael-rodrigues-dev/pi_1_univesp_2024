from django.contrib import admin

# Register your models here.

from .models import Projeto, Material

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    """ Classe admin para o Projeto """
    list_display = ("nome", "dt_criacao")


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    """ Classe admin para o Material """
    list_display = ("nome", "unidade_medida")
