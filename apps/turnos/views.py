from django.shortcuts import render
from django.views.generic.edit import CreateView
from apps.clientes.models import Cliente

from apps.turnos.models import Turno
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect
from django.contrib.messages.api import success
from apps.turnos.forms import TurnoForm

class RegistrarTurno(CreateView):
    template_name='turnos/registrarTurno.html'
    form_class = TurnoForm
    
    def form_valid(self, form):
        self.object = form.save(commit= False)
        self.object.usu = self.request.user
        self.object.estado = "Pendiente"
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('mostrar_turno'))
    
    success_url=reverse_lazy('mostrar_turno')

    
class mostrarTurno(ListView):
    template_name='turnos/mostrarTurno.html'
    model=Turno
    context_object_name= 'turnoListaObjetos'