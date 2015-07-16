from django.conf.urls import patterns, include, url
from apps.turnos.views import RegistrarTurno, mostrarTurno



urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarTurno.as_view(),name="registrar_turno"),
    url(r'^mostrar/$', mostrarTurno.as_view(),name="mostrar_turno")
   
)
