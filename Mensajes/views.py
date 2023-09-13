from .models import Mensaje
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User  # Importa el modelo User
from .forms import MensajeForm



@login_required
def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user  # Asigna el remitente como el usuario logueado
            mensaje.save()
            return redirect('Mensajes:ver_mensajes')
    else:
        form = MensajeForm()

    return render(request, 'Mensajes/crear_mensaje.html', {'form': form})






@login_required
def ver_mensajes(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'Mensajes/ver_mensajes.html', {'mensajes': mensajes})


