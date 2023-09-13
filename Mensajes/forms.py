# forms.py
from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']  # Los campos que deseas incluir en el formulario

    # def __init__(self, *args, **kwargs):
    #     destinatarios = kwargs.pop('destinatarios', None)  # Obtiene el queryset de destinatarios si se proporciona
    #     super(MensajeForm, self).__init__(*args, **kwargs)

    #     # Excluye al usuario remitente que está logeado
    #     if destinatarios is not None:
    #         self.fields['destinatario'].queryset = destinatarios.exclude(pk=self.instance.remitente.pk)


