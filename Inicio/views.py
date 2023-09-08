from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import   AuthenticationForm, UserCreationForm
from .forms import registro_usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    return render(request, 'Inicio/inicio.html')


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "Inicio/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request,"Inicio/login.html", {"form":form, "mensaje":"Datos invalidos"})
        else:
            return render(request,"Inicio/login.html", {"form":form, "mensaje":"Datos invalidos"})
    else:
        form=AuthenticationForm()
        return render(request,"Inicio/login.html", {"form":form})
    

def register(request):
    if request.method=="POST":
        form=registro_usuario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save() 
            return render(request, "Inicio/inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente"})
        else:
            return render(request,"Inicio/register.html", {"form":form, "mensaje":"Datos invalidos"})
    else:
        form=registro_usuario()
        return render(request,"Inicio/register.html", {"form":form})    
    