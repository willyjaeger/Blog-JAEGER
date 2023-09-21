from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'administrador'  # Esto establece el espacio de nombres de la aplicación



urlpatterns = [
    path('administrador/adminusuariolistar/', views.adminusuarioLista, name='adminusuariolista'),
    path('administrador/administrador/', views.administrador, name='administrador'),
    path('administrador/adminusuarioeditar/<int:pk>/', views.adminusuariEditar, name='adminusuarioeditar'),
    path('administrador/adminusuarioeliminar/<int:user_id>/', views.adminusuarioEliminar, name='adminusuarioeliminar'),  
    path('administrador/adminposteoeditar/<int:pk>/', views.adminposteoEditar, name='adminposteoeditar'),
    path('administrador/adminposteoeliminar/<int:user_id>/', views.adminposteoEliminar, name='adminposteoeliminar'),      
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


