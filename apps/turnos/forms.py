from django import forms
from apps.turnos.models import Turno
from django.forms import ModelForm
from apps.profesionales.models import Profesional


class TurnoForm(ModelForm):
    pro = forms.ModelChoiceField(Profesional.objects.all(), required = True)
    
    
    class Meta:
        model = Turno;
        fields = ("pro", "fechahora", "comentario",)
    