from django.db import models

class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    documento=models.IntegerField()
    telefono=models.IntegerField()
    obrasocial=models.CharField(max_length=50)
    email= models.EmailField(max_length=75)
    clave=models.CharField(max_length=50)
    reingresarclave=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre