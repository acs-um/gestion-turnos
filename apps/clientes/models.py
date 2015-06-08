from django.db import models
from django.contrib.auth.models import User

class PerfilCliente(models.Model):
    usuario= models.OneToOneField(User)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    documento=models.IntegerField()
    telefono=models.IntegerField()
    obrasocial=models.CharField(max_length=50)
    email= models.EmailField(max_length=75)
    
    
    def __unicode__(self):
        return self.usuario.username