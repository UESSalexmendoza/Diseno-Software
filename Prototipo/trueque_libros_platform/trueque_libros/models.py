from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='libros/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class SolicitudTrueque(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]

    libro_ofrecido = models.ForeignKey(Libro, related_name='libros_ofrecidos', on_delete=models.CASCADE)
    libro_deseado = models.ForeignKey(Libro, related_name='libros_deseados', on_delete=models.CASCADE)
    usuario_ofrecido = models.ForeignKey(User, related_name='usuarios_ofrecidos', on_delete=models.CASCADE)
    usuario_deseado = models.ForeignKey(User, related_name='usuarios_deseados', on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f'{self.libro_ofrecido} ⇄ {self.libro_deseado} ({self.estado})'
