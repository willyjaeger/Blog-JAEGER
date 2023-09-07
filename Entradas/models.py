from django.db import models

# Create your models here.
class EntradasBlog(models.Model):
    fecha=models.DateTimeField(null=False)   
    titulo=models.CharField(max_length=40,null=False,default="") 
    subtitulo=models.CharField(max_length=40,null=False,default="")
    contenido=models.CharField(max_length=100,null=False,default="")
    usuarioid=models.IntegerField()
    autor=models.CharField(max_length=40,null=False,default="")
    imagen=models.CharField(max_length=40,null=False,default="")
    def __str__(self):
        return f"{self.fecha} - {self.titulo} - {self.contenido} - {self.autor} "