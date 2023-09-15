from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import registro_usuario, EditarUsuarioForm, editar_usuario, Avatarform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Avatar 
import requests
from bs4 import BeautifulSoup
from Entradas.models import Entrada


# ...

# Create your views here.

def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    
    if len(avatares)!=0:
        
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"




def posteosRecientes():
    entradas_recientes = Entrada.objects.order_by('-id')[:4]  # Obtener las últimas 4 entradas (o las que desees)
    return entradas_recientes

def inicio(request):
    avatar = obtenerAvatar(request)
    entradas_recientes = posteosRecientes()
    return render(request, 'Inicio/inicio.html', {"avatar": avatar, "entradas_recientes": entradas_recientes})

def todaslasEntradas(request):
    entradas = Entrada.objects.all()
    num_entradas = len(entradas)
    return render(request, 'Entradas/entradalista.html', {'entradas': entradas, 'num_entradas': num_entradas})
   


    
def login_request(request):
    avatar= obtenerAvatar(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu = info["username"]
            clave = info["password"]
            usuario = authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "Inicio/inicio.html", {"mensaje": f"Usuario {usu} logueado correctamente", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "registration/login.html", {"form": form, "mensaje": "Datos inválidos", "avatar": avatar})

        else:
            return render(request, "registration/login.html", {"form": form, "mensaje": "Datos inválidos", "avatar": avatar})

    else:
        form = AuthenticationForm()
        return render(request, "registration/login.html", {"form": form, "avatar": obtenerAvatar(request)})



def register(request):
    avatar= obtenerAvatar(request)
    if request.method=="POST":
        form=registro_usuario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save() 
            return render(request, "Inicio/inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente", "avatar": obtenerAvatar(request)})
        else:
            avatar=Avatar.objects.filter(user=request.user.id)[0].img.url   
            return render(request,"Inicio/register.html", {"form": form, "mensaje": "Datos inválidos", "avatar": avatar})

    else:
        form=registro_usuario()
        return render(request,"Inicio/register.html", {"form": form, "avatar": obtenerAvatar(request)})
  
 
@login_required
def usuarioeditar(request):
    usuario = request.user

    if request.method == "POST":
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            # Obtener los datos del formulario
            form_data = form.cleaned_data

            # Comparar los valores del formulario con los valores actuales del usuario
            if form_data.get("username") != usuario.username:
                usuario.username = form_data["username"]
            if form_data.get("email") != usuario.email:
                usuario.email = form_data["email"]
            if form_data.get("first_name") != usuario.first_name:
                usuario.first_name = form_data["first_name"]
            if form_data.get("last_name") != usuario.last_name:
                usuario.last_name = form_data["last_name"]

            # Verificar si se ingresó una nueva contraseña
            password = form_data.get("password")
            if password:
                usuario.set_password(password)

            # Guardar los cambios en el usuario
            usuario.save()

            return redirect("inicio")  # Redirigir a la página de inicio o a donde desees
    else:
        form = EditarUsuarioForm(instance=usuario)

    return render(request, "Inicio/usuarioeditar.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)})



# @login_required
# def agregaravatar(request):
#     avatar = obtenerAvatar(request)

#     if request.method == "POST":
#         form = Avatarform(request.POST, request.FILES)
#         if form.is_valid():
#             avatar_nuevo = Avatar(user=request.user, imagen=request.FILES["imagen"])

#             avatar_viejo = Avatar.objects.filter(user=request.user)
#             if avatar_viejo.exists():
#                 avatar_viejo[0].delete()
            
#             avatar_nuevo.save()
#             return render(request, "inicio.html", {"mensaje": f"Avatar agregado correctamente", "avatar": obtenerAvatar(request)})
#         else:
#             return render(request, "Inicio/agregaravatar.html", {"form": form, "usuario": request.user, "mensaje": "Error al agregar el avatar"})
#     else:
#         form = Avatarform()
#         return render(request, "Inicio/agregaravatar.html", {"form": form, "usuario": request.user, "avatar": obtenerAvatar(request)})

# 

@login_required
def agregaravatar(request):
    avatar = obtenerAvatar(request)

    if request.method == "POST":
        form = Avatarform(request.POST, request.FILES)
        if form.is_valid():
            # Procesar el formulario cuando es válido
            avatar_nuevo = Avatar(user=request.user, imagen=request.FILES["imagen"])

            # Eliminar el avatar anterior si existe
            avatar_viejo = Avatar.objects.filter(user=request.user)
            if avatar_viejo.exists():
                avatar_viejo[0].delete()
            
            # Guardar el nuevo avatar
            avatar_nuevo.save()
            return render(request, "inicio.html", {"mensaje": f"Avatar agregado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "Inicio/agregaravatar.html", {"form": form, "mensaje": "Error al agregar el avatar"})
    else:
        # En una solicitud GET, muestra el formulario vacío o con datos iniciales
        form = Avatarform(initial={'usuario': request.user})
        return render(request, "Inicio/agregaravatar.html", {"form": form, "avatar": obtenerAvatar(request)})




