from apps.turnos.models import Turno
from django.forms import ModelForm

class TurnoNotificarFrom(ModelForm):
    class Meta:
        model =Turno;
        fields =('comentario',)
        