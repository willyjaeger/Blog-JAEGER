from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.



class Entrada(models.Model):
    titulo = models.CharField(max_length=160)
    subtitulo = models.CharField(max_length=160)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img/')  # Debes configurar la carga de archivos estáticos

    def __str__(self):
        return f"{self.fecha} - {self.titulo} - {self.contenido} - {self.autor} "





