from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Inicio.views import obtenerAvatar, posteosRecientes
from Inicio.models import Avatar
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserEditForm
# @login_required
# def adminUsuarioDetalle(request, pk):
#     avatar = obtenerAvatar(request)
#     entrada = get_object_or_404(Entrada, pk=pk)
#     entradas_recientes = posteosRecientes()
#     return render(request, 'Entradas/entradadetalle.html', {'entrada': entrada, "entradas_recientes": entradas_recientes, "avatar": avatar})

# from .models import Entrada
from django.shortcuts import render

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
            return redirect('administrador:adminusuarioeditar', pk=usuario.pk)
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





# @login_required
# def adminusuarioCrear(request):
#     avatar= obtenerAvatar(request)
#     if request.method == 'POST':
#         form = EntradaForm(request.POST, request.FILES)
#         if form.is_valid():
#             entrada = form.save(commit=False)
#             entrada.autor = request.user
#             entrada.save()
#             messages.success(request, 'Entrada creada con éxito.')  # Agrega un mensaje de éxito
#             return redirect('Entradas:entradalista')

#     else:
#         form = EntradaForm()
    
#     return render(request, 'Entradas/entradaformulario.html', {'form': form, "avatar": avatar})




# @login_required
# def adminusuarioEditar(request, pk):
#     avatar= obtenerAvatar(request)
#     entrada = get_object_or_404(Entrada, pk=pk)
#     if request.method == 'POST':
#         form = EntradaForm(request.POST, request.FILES, instance=entrada)
#         if form.is_valid():
#             form.save()
#             return redirect('Entradas:entradadetalle', pk=entrada.pk)
#     else:
#         form = EntradaForm(instance=entrada)
#     return render(request, 'Entradas/entradaformulario.html', {'form': form, "avatar": avatar})

# # Create your views here.
