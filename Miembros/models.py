from django.db import models

# Create your models here.

class Miembro(models.Model):
    nickname=models.CharField(max_length=40,null=False,default="") 
    nombre=models.CharField(max_length=40,null=False,default="")
    apellido=models.CharField(max_length=40,null=False,default="")     
    contraseña=models.CharField(max_length=40)
    email=models.EmailField(max_length=40,null=True,default="")
        
    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.nickname} -  {self.email}"