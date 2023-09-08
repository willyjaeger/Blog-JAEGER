from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.models import User


class registro_usuario(UserCreationForm):
    username=forms.CharField(label="Nombre de usuario")
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)   
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput) 
    class Meta:
        model=User
        fields=("username", "email", "password1", "password2", "first_name", "last_name" )
        help_texts={k:"" for k in fields}

        
class editar_usuario(UserCreationForm):
    username=forms.CharField(label="Nombre de usuario")
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)   
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput) 
    first_name=forms.CharField(label="Modificar Nombre")  
    last_name=forms.CharField(label=" Modificar Apellido") 
    class Meta:
        model=User
        fields=("username", "email", "password1", "password2", "first_name", "last_name" )
        help_texts={k:"" for k in fields}

    