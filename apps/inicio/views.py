from django.views.generic import TemplateView, FormView
from apps.inicio.forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles

class Registrar(FormView):
    template_name= 'inicio/registrar.html'
    form_class= UserForm
    success_url= reverse_lazy('login')
    
    def form_valid(self, form):
        user= form.save() #Todo el formulario que es un obj de un usuario se guarda en user
        perfil=Perfiles()
        perfil.usuario=user
        perfil.nombre=form.cleaned_data['nombre']
        perfil.apellido=form.cleaned_data['apellido']
        perfil.dni=form.cleaned_data['dni']
        perfil.email=form.cleaned_data['email']
        perfil.direccion=form.cleaned_data['direccion']
        perfil.obrasocial=form.cleaned_data['obrasocial']
        perfil.telefono=form.cleaned_data['telefono']
        perfil.save()
        return super(Registrar, self).form_valid(form)