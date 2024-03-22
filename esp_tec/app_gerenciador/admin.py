from django.contrib import admin

# Register your models here.

from .models import Projeto

@admin.register(Projeto)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("nome", "dt_criacao")
