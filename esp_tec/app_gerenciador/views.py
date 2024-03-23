"""
Gerador de PDF
"""

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from app_gerenciador.models import Projeto

from datetime import date


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class ProjectReport(DetailView):
    """
    Classe que herda o DetailView para implementar 
    o Relatório do Projeto
    """
    model = Projeto
    queryset = model.objects.all()
    template_name = "report.html"

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context["hoje"] = date.today()
     return context
