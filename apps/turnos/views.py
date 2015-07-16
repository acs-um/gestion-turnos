from django.shortcuts import render, render_to_response
from django.views.generic.edit import CreateView, UpdateView
from apps.clientes.models import Cliente
from apps.turnos.models import Turno
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import request
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.forms.forms import Form
from django.contrib.messages.api import success
from apps.turnos.forms import TurnoFrom, TurnoBorrarFrom


class RegistrarTurno(CreateView):
    template_name='turnos/registrarTurno.html'
    model=Turno
    success_url=reverse_lazy('mostrar_turno')
    
class mostrarTurno(ListView):
    template_name='turnos/mostrarTurno.html'
    model=Turno
    context_object_name= 'turnoListaObjetos'
    
class borrarTurno(UpdateView):
    model=Turno
    form_class= TurnoBorrarFrom
    template_name= 'turnos/borrarTurno.html'
    
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.usu=self.request.user
        self.object.estado="Cancelado"
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('mostrar_turno'))