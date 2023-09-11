from django.shortcuts import render, get_object_or_404, redirect
from .models import Entrada
from .forms import EntradaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def entradaLista(request):
    entradas = Entrada.objects.all()
    num_entradas = len(entradas)
    print("Número de entradas:", num_entradas)  # Mensaje de depuración
    return render(request, 'Entradas/entradalista.html', {'entradas': entradas, 'num_entradas': num_entradas})


@login_required
def entradaCrear(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.autor = request.user
            entrada.save()
            messages.success(request, 'Entrada creada con éxito.')  # Agrega un mensaje de éxito
            return redirect('entradalista')
    else:
        form = EntradaForm()
    
    return render(request, 'Entradas/entradaformulario.html', {'form': form})


def entradaDetalle(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'Entradas/entradadetalle.html', {'entrada': entrada})

@login_required
def entradaEditar(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('entradadetalle', pk=entrada.pk)
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'Entradas/entradaformulario.html', {'form': form})
