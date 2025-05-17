from django.contrib import admin
from .models import (
    Usuario,
    Perfil,
    TipoContacto,
    FormaContacto,
    Categoria,
    EstadoLibro,
    Libro,
    EstadoPeticion,
    Peticion,
    PeticionHistorial,
    Contacto,
)

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(TipoContacto)
admin.site.register(FormaContacto)
admin.site.register(Categoria)
admin.site.register(EstadoLibro)
admin.site.register(Libro)
admin.site.register(EstadoPeticion)
admin.site.register(Peticion)
admin.site.register(PeticionHistorial)
admin.site.register(Contacto)
