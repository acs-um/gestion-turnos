from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    nombre=forms.CharField()
    apellido=forms.CharField()
    obrasocial=forms.CharField()
    dni=forms.IntegerField()
    direccion=forms.CharField()
    email=forms.EmailField()
    telefono= forms.IntegerField()