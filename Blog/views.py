from django.shortcuts import render
from Entradas.models import Entrada 

def posteosRecientes(request):
    entradas_recientes = Entrada.objects.order_by('-id')[:4]  # Obtener las últimas 4 entradas (o las que desees)
    
    # Renderiza la plantilla adecuada según el contexto
    if request.path == '/Inicio/':
        template_name = 'inicio.html'
    elif request.path == '/Entradas/':
        template_name = 'entradadetalle.html'
    else:
        # Define un comportamiento predeterminado si es necesario
        template_name = 'padre.html'
    
    return render(request, template_name, {'entradas_recientes': entradas_recientes})

def todaslasEntradas(request):
    entradas = Entrada.objects.all()
    num_entradas = len(entradas)
    return render(request, 'entradalista.html', {'entradas': entradas, 'num_entradas': num_entradas})   