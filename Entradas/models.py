from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class EntradasBlog(models.Model):
    fecha=models.DateTimeField(null=False)   
    titulo=models.CharField(max_length=40,null=False,default="") 
    subtitulo=models.CharField(max_length=40,null=False,default="")
    contenido=models.CharField(max_length=100,null=False,default="")
    usuarioid=models.IntegerField()
    autor=models.CharField(max_length=40,null=False,default="")
    imagen=models.CharField(max_length=40,null=False,default="")



class Entrada(models.Model):
    titulo = models.CharField(max_length=160)
    subtitulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img/')  # Debes configurar la carga de archivos estáticos

    def __str__(self):
        return f"{self.fecha} - {self.titulo} - {self.contenido} - {self.autor} "





