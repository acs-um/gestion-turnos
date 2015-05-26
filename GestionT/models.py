from django.db import models

class Usuarios(models.Model):
	usu_id=models.AutoField(primary_key= 1)
	usu_rol=models.CharField(max_length=50)
	usu_email=models.EmailField(max_length=75)
	usu_pass=models.CharField(max_length=50)
	usu_nombre=models.CharField(max_length=50)
	usu_apellido=models.CharField(max_length=50)
	usu_telefono=models.IntegerField()
	usu_dni=models.IntegerField()
	usu_direccion=models.CharField(max_length=50)
	usu_obrasocial=models.CharField(max_length=50)
	usu_estado= models.BooleanField(default=1)

class Turnos(models.Model):
	tur_id=models.AutoField(primary_key=1)
	tur_usu_id=models.IntegerField()
	tur_estado=models.CharField(max_length=50)
	tur_fechahora=models.DateTimeField()
	tur_comentario= models.TextField()