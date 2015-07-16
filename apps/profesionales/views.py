from django.shortcuts import render
from django.views.generic.edit import CreateView
from apps.profesionales.models import Profesional
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

class RegistrarProfesional(CreateView):
    template_name='profesionales/registrarProfesional.html'
    model=Profesional
    success_url=reverse_lazy('mostrar_profesional')
class mostrarProfesional(ListView):
    template_name= 'profesionales/mostrarProfesional.html'
    model=Profesional
    context_object_name= 'profesionalesListaObjetos'