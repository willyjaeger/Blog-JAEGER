# messages/models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Conversacion(models.Model):
    participantes = models.ManyToManyField(User, related_name='conversaciones')


class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, null=True)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.remitente} - {self.destinatario} - {self.contenido} - {self.fecha_envio} - {self.leido}"
