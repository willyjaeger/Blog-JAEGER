from django.urls import path  
from .views import *    
from django.contrib.auth.views import LogoutView

urlpatterns = [ 


    path("",inicio,name="inicio"),

    # LOGIN LOGOUT REGISTER
    path('Inicio/register/', register, name="register"),
    path('Inicio/login/', login_request, name="login"),
    path('Inicio/logout/', LogoutView.as_view(), name="logout"),
    path('Inicio/usuarioeditar/', usuarioeditar, name="usuarioeditar"),
    path('Inicio/agregaravatar/', agregaravatar, name="agregaravatar"),
]


