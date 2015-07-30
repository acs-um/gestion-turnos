from django.conf.urls import patterns, include, url
from apps.secretarios.views import mostrarSecretario, mostrarTurno, RegistrarSecretario,\
    NotificarTurno
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
                       url(r'^registrar/$', RegistrarSecretario.as_view(),name="registrar_secretario"),
                       url(r'^mostrar/$', mostrarSecretario.as_view(),name="mostrar_secretario"),
                       url(r'^mostrarTurno/$', mostrarTurno.as_view(),name="mostrar_turno_secretario"),
                       url(r'^notificarTurno/(?P<pk>\d+)/$', NotificarTurno.as_view(), name='notificar_turno'),
)