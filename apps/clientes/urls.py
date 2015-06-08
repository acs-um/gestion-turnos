from django.conf.urls import patterns, include, url
from apps.clientes.views import RegistrarCliente, mostrarCliente



urlpatterns = patterns('',
                       url(r'^registrar/$', RegistrarCliente.as_view(),name="registrar_cliente"),
                       url(r'^mostrar/$', mostrarCliente.as_view(),name="mostrar_cliente")
)
