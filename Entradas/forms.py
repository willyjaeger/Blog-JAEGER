from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']


class Entries(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    contenido = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()