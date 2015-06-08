from django.db import models
from apps.clientes.models import Cliente
from django.contrib.auth.models import User
from apps.profesionales.models import Profesional

class Turno(models.Model):
    id=models.AutoField(primary_key=True)
    usu=models.ForeignKey(User)
    pro=models.ForeignKey(Profesional)
    estado=models.CharField(max_length=50)
    fechahora=models.DateTimeField()
    comentario= models.TextField()