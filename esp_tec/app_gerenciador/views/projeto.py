"""
View do Projeto
"""
from typing import Any
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.core.paginator import Paginator

from app_gerenciador.models import Projeto
from app_gerenciador.forms.projeto import ProjetoForm
from django.urls import reverse_lazy

@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class ProjetoListView(ListView):
    """
    Classe que herda o ListView para implementar a listagem
    de Projetos
    """
    model =Projeto
    template_name = 'projeto/list.html'
    paginate_by = 10
    paginator_class = Paginator

    def get_queryset(self) -> QuerySet[Any]:
        """
        Sobrescreve o método get_queryset()
        """
        return super().get_queryset().order_by('dt_criacao')


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class ProjetoCreateView(CreateView):
    """
    Classe que herda o CreateView para implementar 
    a criação de Projetos
    """
    model = Projeto
    form_class = ProjetoForm
    template_name = "projeto/form.html"
    success_url = reverse_lazy('projeto_list')
    actions = ['projeto_adicionar']


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class ProjetoUpdateView(UpdateView):
    """
    Classe que herda o ListView para implementar 
    o update de Eventos
    """

    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy('projeto_list')
    template_name = "projeto/form.html"
    actions = ['projeto_editar']


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class ProjetoDeleteView(DeleteView):
    """
    Classe que herda o DeleteView para implementar 
    a exclusão de Projetos
    """
    model = Projeto
    success_url = reverse_lazy('projeto_list')
    template_name = "projeto/delete.html"
