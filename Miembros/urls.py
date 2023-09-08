from django.urls import path    
from .views import *    
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [ 


    path("miembro/lista/",MiembroLista.as_view(),name="miembrolista"),
    path("miembro/crear/",MiembroCrear.as_view(),name="miembrocrear"),         
    path("miembro/<pk>",MiembroDetalle.as_view(),name="miembrodetalle"), 
    path("miembro/borrar/<pk>",MiembroBorrar.as_view(),name="miembroborrar"),   
    path("miembro/editar/<pk>",MiembroEditar.as_view(),name="miembroeditar"),


]   
