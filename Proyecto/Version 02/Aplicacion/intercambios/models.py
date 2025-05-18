from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Perfil(models.Model):
    nombrePerfil = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombrePerfil

class TipoContacto(models.Model):
    tipoContacto = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.tipoContacto

class Usuario(AbstractUser):
    nombreReal = models.CharField(max_length=100)
    fechaAcceso = models.DateTimeField(null=True, blank=True)
    telefono = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    aceptacionPolitica = models.BooleanField(default=False)
    fechaAceptacion = models.DateTimeField(null=True, blank=True)
    intentosFallidos = models.IntegerField(default=0)
    estatus = models.CharField(max_length=20, default='Activo')
    perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, related_name='usuarios')
    contactoPrincipal = models.ForeignKey(TipoContacto, on_delete=models.SET_NULL, null=True,)
    def __str__(self):
        return self.username  

class FormaContacto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='formasContacto')
    tipoContacto = models.ForeignKey(TipoContacto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.nombreReal} - {self.tipoContacto.tipoContacto}"

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreCategoria

class EstadoLibro(models.Model):
    estado = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.estado
def ruta_portadas(instance, filename):
    return f'portadas/{instance.nombre}_{filename}'

class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    estadoLibro = models.ForeignKey(EstadoLibro, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='libros')
    estadoRegistro = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to=ruta_portadas, null=True, blank=True)    
    vistas = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.nombre} ({self.autor}) - {self.estadoLibro.estado}"

class EstadoPeticion(models.Model):
    estado = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.estado

class Peticion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='peticiones')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='fk_libros')
    libroIntercambio = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='fk_libros_solicitudes')
    fechaPeticion = models.DateTimeField(auto_now_add=True)
    estadoPeticion = models.ForeignKey(EstadoPeticion, on_delete=models.SET_NULL, null=True)
    fechaLimiteDevolucion = models.DateTimeField(null=True, blank=True)
    mensaje = models.TextField(blank=True)
    respuesta = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.nombreReal} → {self.libro.nombre} ({self.estadoPeticion})"


class PeticionHistorial(models.Model):
    peticion = models.ForeignKey(Peticion, on_delete=models.CASCADE, related_name='historial')
    estado = models.ForeignKey(EstadoPeticion, on_delete=models.SET_NULL, null=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    usuarioResponsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    comentario = models.TextField(blank=True)
    def __str__(self):
        return f"{self.peticion.id} - {self.estado.estado} ({self.fechaCambio.strftime('%Y-%m-%d %H:%M')})"

class Contacto(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    comentario = models.TextField(max_length=1000)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.correo}"
