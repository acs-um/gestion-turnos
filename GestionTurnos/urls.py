from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    
   url(r'^admin/', include(admin.site.urls)),
   #INICIO
   url(r'^', include('apps.inicio.urls')),
   #CLIENTES
   url(r'^cliente/', include('apps.clientes.urls')),
   #TURNOS
   url(r'^turno/', include('apps.turnos.urls')),
   #PROFESIONALES
   url(r'^profesional/', include('apps.profesionales.urls')),
   #SECRETARIOS
   url(r'^secretario/', include('apps.secretarios.urls')),
   
)
