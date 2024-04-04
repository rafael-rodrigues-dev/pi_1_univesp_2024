"""
URL configuration for esp_tec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_gerenciador.views import ProjectReport, ViewPDF, home

from app_gerenciador.views.projeto import (
    ProjetoListView, 
    ProjetoCreateView, 
    ProjetoUpdateView,
    ProjetoDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path('report/<int:pk>/',
        ProjectReport.as_view(),
        name = 'report'
    ),
    path('report_pdf/<int:pk>/',
        ViewPDF.as_view(),
        name = 'report_pdf'
    ),
    path('projeto/',
        ProjetoListView.as_view(),
        name = 'projeto_list'
    ),
    path('projeto/adicionar',
        ProjetoCreateView.as_view(),
        name = 'projeto_adicionar'
    ),
    path('projeto/editar/<int:pk>/',
        ProjetoUpdateView.as_view(),
        name = 'projeto_editar'
    ),
     path(
        'projeto/delete/<int:pk>/',
        ProjetoDeleteView.as_view(),
        name = 'projeto_delete'
    ),
    path('', home, name='home')
]
