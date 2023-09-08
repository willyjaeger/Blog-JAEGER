from django.shortcuts import render
from .models import  Miembro
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView, PasswordChangeView  
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def miembroregistro(request):
    if request.method=="POST":
        nickname=request.POST["nickname"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        contraseña=request.POST["contraseña"]
        email=request.POST["email"]
        miembro=Miembro(nickname=nickname,nombre=nombre,apellido=apellido,contraseña=contraseña,email=email)
        miembro.save()

        return render(request,"miembroregistro.html",{"mensaje":"Miembro Registrado"})
    else:

        return render(request,"miembroregistro.html")   
    return render(request, 'Miembros/miembroregistro.html')

@login_required
def miembroeditar(request):
    return render(request, 'Miembros/miembroeditar.ntml')

class MiembroLista(LoginRequiredMixin,ListView):
    model = Miembro
    template_name = 'Miembros/miembrolista.html'

class MiembroCrear(LoginRequiredMixin,CreateView):
    model = Miembro

    fields = ['nickname','nombre','apellido','contraseña','email']
    template_name = 'Miembros/miembroeditar.html'
    success_url = reverse_lazy('miembrolista' )

class MiembroDetalle(LoginRequiredMixin,DetailView):
    model = Miembro
    template_name = 'Miembros/miembrodetalle.html'

class MiembroBorrar(LoginRequiredMixin,DeleteView):
    model = Miembro
    template_name = 'Miembros/miembro_confirm_delete.html'
    success_url = reverse_lazy('miembrolista' )

class MiembroEditar(LoginRequiredMixin,UpdateView):
    model = Miembro
    fields = ['nickname','nombre','apellido','contraseña','email']
    template_name = 'Miembros/miembroeditar.html'
    success_url = reverse_lazy('miembrolista' )