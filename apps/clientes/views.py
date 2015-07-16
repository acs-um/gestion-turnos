from django.shortcuts import render
from django.views.generic.edit import FormView
from apps.clientes.models import PerfilCliente
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from apps.clientes.forms import UserForm
from django.views.generic.list import ListView

class RegistrarCliente(FormView):
    template_name='clientes/registrarCliente.html'
    form_class=UserForm
    success_url=reverse_lazy('mostrar_cliente')
    
    def form_valid(self, form):
        user= form.save()
        perfil=PerfilCliente()
        perfil.usuario=user
        perfil.nombre=form.cleaned_data['nombre']
        perfil.apellido=form.cleaned_data['apellido']
        perfil.documento=form.cleaned_data['documento']
        perfil.email=form.cleaned_data['email']
        perfil.obrasocial=form.cleaned_data['obrasocial']
        perfil.telefono=form.cleaned_data['telefono']
        perfil.save()
        return super(RegistrarCliente, self).form_valid(form)
    
class MostrarCliente(ListView):
    template_name= 'clientes/mostrarCliente.html'
    model=PerfilCliente
    context_object_name= 'clientesListaObjetos'
    
    