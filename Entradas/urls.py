from django.urls import path    
from .views import *    
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [ 



    # login logout register

    #path('login/', llamologin, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]   
