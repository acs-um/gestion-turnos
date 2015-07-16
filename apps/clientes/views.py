from django.shortcuts import render
from django.views.generic.edit import CreateView
from apps.clientes.models import Cliente
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

class RegistrarCliente(CreateView):
    template_name='clientes/registrarCliente.html'
    model=Cliente
    success_url=reverse_lazy('mostrar_cliente')
class mostrarCliente(ListView):
    template_name= 'clientes/mostrarCliente.html'
    model=Cliente
    context_object_name= 'clientesListaObjetos'
    
    