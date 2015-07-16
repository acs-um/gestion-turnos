from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    nombre=forms.CharField()
    apellido=forms.CharField()
    documento=forms.IntegerField()
    telefono=forms.IntegerField()
    obrasocial=forms.CharField()
    email= forms.EmailField()