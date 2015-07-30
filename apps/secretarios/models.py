from django.db import models
from django import forms

class Secretario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    documento=models.IntegerField()
    telefono=models.IntegerField()
    email= models.EmailField(max_length=75)
    clave=models.CharField(max_length=50)
    reingresarclave=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre

class EmailForm(models.Model):
    subject = models.CharField(max_length = 75)
    message = models.CharField(max_length = 500)