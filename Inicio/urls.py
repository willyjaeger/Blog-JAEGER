from django.urls import path  
from .views import *    
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [ 


    path("",inicio,name="inicio"),

    # LOGIN LOGOUT REGISTER
    path('Inicio/register/', register, name="register"),
   
    path('Inicio/logout/', LogoutView.as_view(), name="logout"),
    path('Inicio/usuarioeditar/', usuarioeditar, name="usuarioeditar"),
    path('Inicio/agregaravatar/', agregaravatar, name="agregaravatar"),
    path('Inicio/about/', views.about, name="about"),
]


