from django import forms
from django.contrib.auth.models import User
from Entradas.models import Entrada

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_superuser', 'groups']

    def clean_username(self):
        username = self.cleaned_data['username']
        user_id = self.instance.id if self.instance else None
        # Validación personalizada para asegurarse de que el nombre de usuario sea único
        if User.objects.filter(username=username).exclude(id=user_id).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')
        return username


class EntradaEditForm(forms.ModelForm):
    class Meta:
        model = Entrada
        exclude = ['fecha']  # Excluye el campo 'fecha' del formulario
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor']

