from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'Entradas'  # Esto establece el espacio de nombres de la aplicación



urlpatterns = [
    path('Entradas/entradalista/', views.entradaLista, name='entradalista'),
    path('Entradas/entradaCrear/', views.entradaCrear, name='entradacrear'),
    path('Entradas/editar/<int:entrada_id>/', views.entradaEditar, name='entradaeditar'),
    path('Entradas/<int:pk>/', views.entradaDetalle, name='entradadetalle'),
    path('Entradas/<int:pk>/edit/', views.entradaEditar, name='entradaeditar'),
    #path('ver_entrada/<int:entrada_id>/', views.entradaDetalle, name='entradadetalle'),
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
