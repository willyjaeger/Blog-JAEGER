from django.shortcuts import render, get_object_or_404, redirect
from .models import Entrada
from .forms import EntradaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Inicio.views import obtenerAvatar, posteosRecientes, todaslasEntradas
from Inicio.models import Avatar
 

def entradaDetalle(request, pk):
    avatar = obtenerAvatar(request)
    entrada = get_object_or_404(Entrada, pk=pk)
    entradas_recientes = posteosRecientes()
    return render(request, 'Entradas/entradadetalle.html', {'entrada': entrada, "entradas_recientes": entradas_recientes})

def entradaLista(request):
    entradas = Entrada.objects.all()
    print(entradas)  # Verifica si se están recuperando las entradas
    num_entradas = len(entradas)
    entradas_recientes = posteosRecientes()
    return render(request, 'Entradas/entradalista.html', {'entradas': entradas, 'num_entradas': num_entradas, "entradas_recientes": entradas_recientes})


# def entradaLista(request):
#     avatar = obtenerAvatar(request)
#     entradas = todaslasEntradas()
#     num_entradas = len(entradas)
#     return render(request, 'Entradas/entradalista.html', {'entradas': entradas, 'num_entradas': num_entradas, "avatar": avatar})


@login_required
def entradaCrear(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.autor = request.user
            entrada.save()
            messages.success(request, 'Entrada creada con éxito.')  # Agrega un mensaje de éxito
            return redirect('Entradas:entradalista')

    else:
        form = EntradaForm()
    
    return render(request, 'Entradas/entradaformulario.html', {'form': form})




@login_required
def entradaEditar(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('Entradas:entradadetalle', pk=entrada.pk)
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'Entradas/entradaformulario.html', {'form': form})
