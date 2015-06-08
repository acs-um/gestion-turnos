from django.shortcuts import render
from django.views.generic.edit import CreateView
from apps.clientes.models import Cliente

from apps.turnos.models import Turno
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

class RegistrarTurno(CreateView):
    template_name='turnos/registrarTurno.html'
    model=Turno
    success_url=reverse_lazy('mostrar_turno')
class mostrarTurno(ListView):
    template_name='turnos/mostrarTurno.html'
    model=Turno
    context_object_name= 'turnoListaObjetos'