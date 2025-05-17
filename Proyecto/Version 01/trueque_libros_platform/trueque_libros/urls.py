from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('solicitar/<int:libro_id>/', views.solicitar_trueque, name='solicitar_trueque'),
    
    # Nuevas rutas para autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
