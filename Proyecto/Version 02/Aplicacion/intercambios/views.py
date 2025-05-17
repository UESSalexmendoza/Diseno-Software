from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse

from django.utils import timezone
from django.urls import reverse_lazy

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.views import PasswordChangeView

from .forms import CustomLoginForm
from .forms import CustomPasswordResetForm
from .forms import CustomSetPasswordForm
from .forms import UsuarioCreationForm
from .forms import ContactoForm
from .forms import UsuarioUpdateForm
from .forms import CustomPasswordChangeForm
from .forms import LibroForm
from .forms import SolicitudIntercambioForm

from .models import Usuario
from .models import Perfil
from .models import EstadoLibro
from .models import Libro
from .models import FormaContacto
from .models import EstadoPeticion
from .models import Peticion

from django.views.generic import ListView

from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

def inicio(request):
    return render(request, 'intercambios/inicio.html')

class CustomLoginView(LoginView):
    template_name = 'intercambios/seguridad/login.html'
    redirect_authenticated_user = True
    authentication_form = CustomLoginForm

def logout_view(request):
    logout(request)
    return redirect('/')

    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'intercambios/seguridad/password_reset.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'intercambios/seguridad/password_reset_email.html'
    subject_template_name = 'intercambios/seguridad/password_reset_subject.txt'
    success_url = '/reset/enviado/'
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'intercambios/seguridad/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = '/reset/completado/'


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'intercambios/seguridad/registro.html'
    def get_success_url(self):
        return reverse_lazy('registro_exitoso')

    def form_valid(self, form):
        form.instance.fechaAceptacion = timezone.now() if form.cleaned_data['aceptacionPolitica'] else None
        user = form.save(commit=False)
        user.estado = False
        user.is_active = False
        try:
            perfil_usuario = Perfil.objects.get(nombrePerfil__iexact='usuario')
            user.perfil = perfil_usuario
        except Perfil.DoesNotExist:
            messages.error(self.request, "Error: el perfil 'usuario' no existe.")
            return self.form_invalid(form)        
        user.save()

        contacto = user.contactoPrincipal
        if contacto:
            FormaContacto.objects.create(usuario=user, tipoContacto=contacto)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_link = self.request.build_absolute_uri(
            reverse('activar_cuenta', kwargs={'uidb64': uid, 'token': token})
        )
        subject = 'Activa tu cuenta en BookBridge'
        message = render_to_string('intercambios/seguridad/email_activacion.html', {
            'user': user,
            'activation_link': activation_link
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
        return super().form_valid(form)

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    template_name = 'intercambios/seguridad/perfil_editar.html'
    success_url = reverse_lazy('perfil_actualizado')

    def get_object(self):
        return self.request.user
    
class UsuarioPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm    
    template_name = 'intercambios/seguridad/cambiar_clave.html'
    success_url = reverse_lazy('clave_cambiada_exitosamente')
    
def clave_cambiada_exitosamente(request):
    return render(request, 'intercambios/seguridad/clave_cambiada_exito.html')
    
def registro_exitoso(request):
    return render(request, 'intercambios/seguridad/registro_exitoso.html')

def activar_cuenta(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Usuario.objects.get(pk=uid)
        print("Usuario:", user.username)       
    except (TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
        user = None

    if user is not None:
        user.estado = True
        user.is_active = True
        user.save()
        user.refresh_from_db()
        messages.success(request, 'Tu cuenta ha sido activada correctamente.')
        return redirect('cuenta_activada')
    else:
        messages.error(request, 'El enlace de activación no es válido o ha expirado.')
        return render(request, 'intercambios/seguridad/activacion_invalida.html')

def perfil_actualizado(request):
    return render(request, 'intercambios/seguridad/perfil_actualizado.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exito')
    else:
        form = ContactoForm()
    return render(request, 'intercambios/contacto/contacto.html', {'form': form})

def contacto_exito(request):
    return render(request, 'intercambios/contacto/contacto_exito.html')

    
def politica_privacidad(request):
    return render(request, 'intercambios/politicas/politica_privacidad.html')

def terminos_condiciones(request):
    return render(request, 'intercambios/politicas/terminos_condiciones.html')

def cuenta_activada(request):
    return render(request, 'intercambios/seguridad/cuenta_activada.html')

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'intercambios/libros/publicar_libro.html'
    success_url = reverse_lazy('libros_mis_libros')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            estado_cargado = EstadoLibro.objects.get(estado__iexact='Cargado')
            form.instance.estadoLibro = estado_cargado
        except EstadoLibro.DoesNotExist:
            form.add_error(None, 'No se encontró el estado "Cargado" en la base de datos.')
            return self.form_invalid(form)        
        return super().form_valid(form)

class MisLibrosView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'intercambios/libros/mis_libros.html'
    context_object_name = 'libros'

    def get_queryset(self):
        queryset = Libro.objects.filter(usuario=self.request.user).select_related('categoria', 'estadoLibro')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(autor__icontains=query) |
                Q(categoria__nombreCategoria__icontains=query)
            )
        return queryset
    
from django.views.generic import ListView
from django.db.models import Q
from .models import Libro

class LibrosPublicadosView(ListView):
    model = Libro
    template_name = 'intercambios/libros/libros_publicados.html'
    context_object_name = 'libros'

    def get_queryset(self):
        queryset = Libro.objects.filter(estadoLibro__estado__iexact='Publicado')
        if self.request.user.is_authenticated:
            queryset = queryset.exclude(usuario=self.request.user)

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(autor__icontains=query) |
                Q(categoria__nombreCategoria__icontains=query) |
                Q(estadoLibro__estado__icontains=query) |
                Q(usuario__nombreReal__icontains=query)
            )

        return queryset.select_related('categoria', 'estadoLibro', 'usuario')


def incrementar_vista_libro(request, pk):
    if request.method == 'POST':
        try:
            libro = Libro.objects.get(pk=pk)
            libro.vistas += 1
            libro.save(update_fields=['vistas'])
            return JsonResponse({'success': True, 'vistas': libro.vistas})
        except Libro.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Libro no encontrado'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

@login_required
def solicitud_intercambio_form(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    # Tus libros publicados (para el select)
    libros_usuario = Libro.objects.filter(usuario=request.user, estadoLibro__estado__iexact='Publicado')

    form = SolicitudIntercambioForm()
    form.fields['libro_ofrecido'].queryset = libros_usuario  # limitamos el queryset

    return render(request, 'intercambios/libros/modal_solicitud.html', {
        'libro': libro,
        'form': form
    })


from datetime import timedelta
@login_required
@require_POST
def crear_peticion(request):
    libro_id = request.POST.get('libro_id')
    libro = get_object_or_404(Libro, id=libro_id)

    libro_ofrecido_id = request.POST.get('libro_ofrecido')
    mensaje = request.POST.get('mensaje')

    libro_ofrecido = get_object_or_404(Libro, id=libro_ofrecido_id, usuario=request.user)

    estado = get_object_or_404(EstadoPeticion, estado__iexact='Pendiente')

    Peticion.objects.create(
        usuario=request.user,
        libro=libro,
        libroIntercambio=libro_ofrecido,
        estadoPeticion=estado,
        fechaPeticion=timezone.now(),
        fechaLimiteDevolucion=timezone.now() + timedelta(days=15),
        mensaje=mensaje,
        respuesta='',
    )
    messages.success(request, 'Tu solicitud fue registrada correctamente.')
    return redirect('libros_publicados')  

@method_decorator(login_required, name='dispatch')
class MisSolicitudesView(ListView):
    model = Peticion
    template_name = 'intercambios/libros/mis_solicitudes.html'
    context_object_name = 'peticiones'

    def get_queryset(self):
        return Peticion.objects.filter(usuario=self.request.user).select_related(
            'libro', 'libro__categoria', 'libro__usuario',
            'libroIntercambio', 'libroIntercambio__categoria',
            'estadoPeticion'
        ).order_by('-fechaPeticion')
        
@login_required
def cancelar_peticion(request, peticion_id):
    peticion = get_object_or_404(Peticion, id=peticion_id, usuario=request.user)

    if peticion.estadoPeticion.estado.lower() == "pendiente":
        estado_cancelado = EstadoPeticion.objects.filter(estado__iexact='Cancelado').first()
        if estado_cancelado:
            peticion.estadoPeticion = estado_cancelado
            peticion.save()
            messages.success(request, "La solicitud fue cancelada correctamente.")
        else:
            messages.error(request, "No se pudo cancelar la solicitud (estado 'Cancelada' no encontrado).")
    else:
        messages.warning(request, "Solo puedes cancelar solicitudes pendientes.")

    return redirect('mis_solicitudes')


@login_required
def solicitudes_recibidas(request):
    solicitudes = Peticion.objects.filter(
        libro__usuario=request.user,
        estadoPeticion__estado__in=['Pendiente', 'En Revision']
    ).select_related('libro', 'usuario', 'estadoPeticion', 'libro__usuario', 'libroIntercambio')

    return render(request, 'intercambios/libros/solicitudes_recibidas.html', {
        'solicitudes': solicitudes
    })


@require_POST
@login_required
def actualizar_estado_peticion(request, peticion_id):
    nuevo_estado = request.POST.get('estado')
    respuesta = request.POST.get('respuesta', '')

    try:
        peticion = Peticion.objects.get(id=peticion_id, libro__usuario=request.user)
        estado_obj = EstadoPeticion.objects.get(estado__iexact=nuevo_estado)
        peticion.estadoPeticion = estado_obj
        peticion.respuesta = respuesta
        peticion.save()
        if nuevo_estado.lower() == 'aprobado':
            estado_intercambiado = EstadoLibro.objects.get(estado__iexact='Intercambiado')
            peticion.libro.estadoLibro = estado_intercambiado
            peticion.libro.save()        
        return JsonResponse({'success': True})
    except Peticion.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Petición no encontrada'})
    except EstadoPeticion.DoesNotExist:
        return JsonResponse({'success': False, 'error': f'El estado "{nuevo_estado}" no existe'})
