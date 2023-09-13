from django.urls import path
from . import views

app_name = 'Mensajes'  # Define el nombre de la aplicación

urlpatterns = [
    path('crear_mensaje/', views.crear_mensaje, name='crear_mensaje'),
    path('ver_mensajes/', views.ver_mensajes, name='ver_mensajes'),
]
