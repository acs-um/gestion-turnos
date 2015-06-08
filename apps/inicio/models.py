from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
    usuario=models.OneToOneField(User)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    obrasocial=models.CharField(max_length=50)
    dni=models.IntegerField()
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono= models.IntegerField()
    
def __unicode__ (self):
    return self.usuario.username