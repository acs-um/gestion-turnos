from django.conf.urls import patterns, include, url
from apps.profesionales.views import mostrarProfesional, RegistrarProfesional

urlpatterns = patterns('',
                       url(r'^registrar/$', RegistrarProfesional.as_view(),name="registrar_profesional"),
                       url(r'^mostrar/$', mostrarProfesional.as_view(),name="mostrar_profesional")
)