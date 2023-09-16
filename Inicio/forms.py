from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.models import User
from .models import Avatar

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



class EditarUsuarioForm(UserChangeForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        required=False  # Hacer que el campo de contraseña sea opcional
    )
    confirm_password = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        required=False  # Hacer que el campo de confirmación de contraseña sea opcional
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(EditarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["readonly"] = True  # Hacer el campo de usuario de solo lectura

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Validar que la contraseña y su confirmación coincidan si se proporciona una contraseña
        if password and password != confirm_password:
            self.add_error("confirm_password", "Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")




class Avatarform(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
