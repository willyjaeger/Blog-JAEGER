from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Inicio.views import obtenerAvatar
from Inicio.models import Avatar
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserEditForm
from django.shortcuts import render
from Entradas.models import Entrada 
from .forms import EntradaEditForm  # Importa el nuevo formulario

# # Create your views here.
@login_required
def administrador(request):
    avatar= obtenerAvatar(request)
    return render(request, 'administrador/administrador.html', {"avatar": avatar})


@login_required

def adminusuarioLista(request):
    avatar= obtenerAvatar(request)
    usuarios = User.objects.all()     #.order_by('-fecha')
    print(usuarios)  # Verifica si se están recuperando las usuarios
    num_usuarios = len(usuarios)
    adminusuariolista_url = reverse('administrador:adminusuariolista')      # Crea la URL para redireccionar        
    return render(request, 'administrador/adminusuariolistar.html', {'adminusuariolista_url': adminusuariolista_url, 'usuarios': usuarios, 'num_usuarios': num_usuarios,  "avatar": avatar})
   # return render(request, 'administrador/adminusuariolistar.html', {'usuarios': usuarios, 'num_usuarios': num_usuarios,  "avatar": avatar})


@login_required
def adminusuariEditar(request, pk):
    avatar = obtenerAvatar(request)
    usuario = get_object_or_404(User, pk=pk)  # Obtén el usuario correcto según la clave primaria (pk)
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('administrador:adminusuariolista')
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'administrador/adminusuarioeditar.html', {'form': form, "avatar": avatar, 'usuario_editado': usuario})
  #  return render(request, 'administrador/adminusuarioeditar.html', {'form': form, 'usuario_editado': usuario})


def adminusuarioEliminar(request, user_id):
    try:
        usuario = User.objects.get(id=user_id)
        usuario.delete()
        messages.success(request, 'El usuario se ha eliminado correctamente.')
    except User.DoesNotExist:
     
        messages.error(request, 'El usuario no existe.')

    return redirect('administrador:adminusuariolista') 

##############################################################################################################
def adminposteoLista(request):
    avatar= obtenerAvatar(request)
    posteos = Entrada.objects.all()     #.order_by('-fecha')
    # print(posteos)  # Verifica si se están recuperando las posteos
    num_posteos = len(posteos)
    adminposteolista_url = reverse('administrador:adminposteolista')      # Crea la URL para redireccionar        
    return render(request, 'administrador/adminposteolistar.html', {'adminposteolista_url': adminposteolista_url, 'posteos': posteos, 'num_posteos': num_posteos,  "avatar": avatar})
   
# @login_required
# def adminposteoEditar(request, pk):
#     avatar = obtenerAvatar(request)
#     posteo = get_object_or_404(Entrada, pk=pk)  # Obtén el posteo correcto según la clave primaria (pk)
#     if request.method == 'POST':
#         form = UserEditForm(request.POST, request.FILES, instance=posteo)
#         if form.is_valid():
#             form.save()
#             return redirect('administrador:adminposteolista')
#     else:
#         form = UserEditForm(instance=posteo)
#     return render(request, 'administrador/adminposteoeditar.html', {'form': form, "avatar": avatar, 'posteo_editado': posteo})
 


# @login_required
# def adminposteoEditar(request, pk):
#     avatar = obtenerAvatar(request)
#     posteo = get_object_or_404(Entrada, pk=pk)
#     usuario = request.user
#     avatar_autor = Avatar.objects.get(user_id=posteo.autor.id)  # Obtén el avatar del autor

#     if request.method == 'POST':
#         form = UserEditForm(request.POST, request.FILES, instance=posteo)
#         if form.is_valid():
#             form.save()
#             return redirect('administrador:adminposteolista')
#         else:
#             print("Formulario no válido. Errores:", form.errors)
#     else:
#         form = UserEditForm(instance=posteo)

#     return render(request, 'administrador/adminposteoeditar.html', {
#         'form': form,
#         'avatar': avatar,
#         'posteo_editado': posteo,
#         'usuario': usuario,
#         'avatar_autor': avatar_autor,
#     })








# @login_required
# def adminposteoEditar(request, pk):
#     avatar = obtenerAvatar(request)
#     posteo = get_object_or_404(Entrada, pk=pk)  # Obtén el posteo correcto según la clave primaria (pk)
#     usuario = request.user  # Obtén el usuario actual

#     if request.method == 'POST':
#         form = UserEditForm(request.POST, request.FILES, instance=posteo)
#         if form.is_valid():
#             form.save()
#             return redirect('administrador:adminposteolista')
#     else:
#         form = UserEditForm(instance=posteo)
    
#     return render(request, 'administrador/adminposteoeditar.html', {'form': form, 'avatar': avatar, 'posteo_editado': posteo, 'usuario': usuario})





def adminposteoEliminar(request, user_id):
    try:
        posteo = Entrada.objects.get(id=user_id)
        posteo.delete()
        messages.success(request, 'El posteo se ha eliminado correctamente.')
    except User.DoesNotExist:
     
        messages.error(request, 'El posteo no existe.')

    return redirect('administrador:adminposteolista') 




@login_required
def adminposteoEditar(request, pk):
    avatar = obtenerAvatar(request)
    posteo = get_object_or_404(Entrada, pk=pk)
    usuario = request.user
    avatar_autor = Avatar.objects.get(user_id=posteo.autor.id)

    if request.method == 'POST':
        form = EntradaEditForm(request.POST, request.FILES, instance=posteo)  # Utiliza el nuevo formulario
        if form.is_valid():
            form.save()
            return redirect('administrador:adminposteolista')
    else:
        form = EntradaEditForm(instance=posteo)  # Utiliza el nuevo formulario

    return render(request, 'administrador/adminposteoeditar.html', {
        'form': form,
        'avatar': avatar,
        'posteo_editado': posteo,
        'usuario': usuario,
        'avatar_autor': avatar_autor,
    })






