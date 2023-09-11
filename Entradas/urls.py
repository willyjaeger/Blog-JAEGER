from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.entradaLista, name='entradalista'),
    path('Entradas/crear/', views.entradaCrear, name='entradacrear'),
    path('Entradas/editar/<int:entrada_id>/', views.entradaEditar, name='entradaeditar'),
    path('Entradas/<int:pk>/', views.entradaDetalle, name='entradadetalle'),
    path('Entradas/<int:pk>/edit/', views.entradaEditar, name='entradaeditar'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

