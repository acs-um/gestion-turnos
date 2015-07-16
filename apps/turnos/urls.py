from django.conf.urls import patterns, include, url
from apps.turnos.views import RegistrarTurno, mostrarTurno, borrarTurno



urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarTurno.as_view(),name="registrar_turno"),
    url(r'^mostrar/$', mostrarTurno.as_view(),name="mostrar_turno"),
    url(r'^borrar/(?P<pk>\d+)/$',borrarTurno.as_view(),name="eliminar_turno"),
   
)
