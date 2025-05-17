from django.urls import path
from . import views
from .views import CustomLoginView
from .views import CustomPasswordResetView
from .views import CustomPasswordResetConfirmView
from .views import UsuarioCreateView
from .views import activar_cuenta
from .views import politica_privacidad
from .views import terminos_condiciones
from .views import registro_exitoso
from .views import cuenta_activada
from .views import contacto
from .views import contacto_exito
from .views import UsuarioUpdateView
from .views import perfil_actualizado
from .views import UsuarioPasswordChangeView
from .views import clave_cambiada_exitosamente
from .views import LibroCreateView
from .views import MisLibrosView
from .views import LibrosPublicadosView
from .views import incrementar_vista_libro
from .views import MisSolicitudesView
from .views import cancelar_peticion
from .views import solicitudes_recibidas



from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('reset/', CustomPasswordResetView.as_view(), name='reset'),
    path('reset/confirmar/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm' ),
    path('reset/enviado/', PasswordResetDoneView.as_view(template_name='intercambios/seguridad/password_reset_done.html'), name='password_reset_done'),   
    path('reset/completado/', PasswordResetCompleteView.as_view(template_name='intercambios/seguridad/password_reset_complete.html'), name='password_reset_complete' ), 
    path('activar/<uidb64>/<token>/', activar_cuenta, name='activar_cuenta'),    
    path('registro/', UsuarioCreateView.as_view(), name='registro'),
    path('registro/exitoso/', registro_exitoso, name='registro_exitoso'),  
    path('cuenta/activada/', cuenta_activada, name='cuenta_activada'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('mi-perfil/editar/', UsuarioUpdateView.as_view(), name='perfil_editar'),    
    path('politica-privacidad/', politica_privacidad, name='politica_privacidad'),    
    path('terminos-condiciones/', terminos_condiciones, name='terminos_condiciones'),    
    path('contacto/', contacto, name='contacto'),
    path('contacto/exito/', contacto_exito, name='contacto_exito'),    
    path('mi-perfil/actualizado/', perfil_actualizado, name='perfil_actualizado'), 
    path('mi-perfil/cambiar-clave/', UsuarioPasswordChangeView.as_view(), name='cambiar_clave'),
    path('mi-perfil/clave-cambiada/',  clave_cambiada_exitosamente , name='clave_cambiada_exitosamente'),    
    path('libros/publicar/', LibroCreateView.as_view(), name='publicar_libro'),     
    path('mis-libros/', MisLibrosView.as_view(), name='libros_mis_libros'), 
    path('libros/', LibrosPublicadosView.as_view(), name='libros_publicados'), 
    path('libros/<int:pk>/incrementar-vista/', incrementar_vista_libro, name='incrementar_vista_libro'),   
    path('libros/<int:pk>/solicitar-form/', views.solicitud_intercambio_form, name='solicitar_libro_form'),     
    path('libros/crear-peticion/', views.crear_peticion, name='crear_peticion'), 
    path('mis-solicitudes/', MisSolicitudesView.as_view(), name='mis_solicitudes'),    
    path('cancelar-peticion/<int:peticion_id>/', cancelar_peticion, name='cancelar_peticion'),   
    path('mis-libros/solicitudes-recibidas/', solicitudes_recibidas, name='solicitudes_recibidas'),  
    path('peticiones/<int:peticion_id>/actualizar-estado/', views.actualizar_estado_peticion, name='actualizar_estado_peticion'),
]
