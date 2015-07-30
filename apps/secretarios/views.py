# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from apps.secretarios.models import Secretario
from apps.inicio.models import Perfiles
from apps.turnos.models import Turno
from apps.secretarios.forms import TurnoNotificarFrom
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import request
from django.contrib.auth.models import User
from apps.turnos.forms import TurnoForm
from django.conf.urls import url

class RegistrarSecretario(CreateView):
    template_name='secretarios/registrarSecretario.html'
    model=Secretario
    success_url=reverse_lazy('mostrar_secretario')
class mostrarSecretario(ListView):
    template_name= 'secretarios/mostrarSecretario.html'
    model=Secretario
    context_object_name= 'secretariosListaObjetos'
    
class mostrarTurno(ListView):
    template_name='secretarios/mostrarTurnoSecretario.html'
    model=Turno
    context_object_name= 'turnoListaObjetos'

class NotificarTurno(UpdateView):
    model=Turno
    form_class= TurnoNotificarFrom
    template_name= 'secretarios/notificarTurno.html'   
    def form_valid(self,form, **kwargs):
        self.object=form.save(commit=False)
        usuario = Perfiles.objects.get(usuario = self.object.usu) 
        email_recibe = usuario.email
        subject = "Turno cancelado"
        email_manda = settings.EMAIL_HOST_USER
        comentario = self.object.comentario
        if subject and comentario and email_manda:
            try:
                send_mail(subject, comentario, email_manda, [email_recibe], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Error')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
        self.object.notificado=True
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('mostrar_turno_secretario'))
                  