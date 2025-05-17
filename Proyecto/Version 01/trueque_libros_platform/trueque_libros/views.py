from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, SolicitudTrueque
from .forms import LibroForm
from django.contrib.auth.decorators import login_required

def index(request):
    libros = Libro.objects.exclude(usuario=request.user) if request.user.is_authenticated else Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})

@login_required
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user
            libro.save()
            return redirect('index')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

@login_required
def solicitar_trueque(request, libro_id):
    libro_deseado = get_object_or_404(Libro, id=libro_id)
    mis_libros = Libro.objects.filter(usuario=request.user)
    if request.method == 'POST':
        libro_ofrecido_id = request.POST.get('libro_ofrecido')
        libro_ofrecido = get_object_or_404(Libro, id=libro_ofrecido_id)
        SolicitudTrueque.objects.create(
            libro_ofrecido=libro_ofrecido,
            libro_deseado=libro_deseado,
            usuario_ofrecido=request.user,
            usuario_deseado=libro_deseado.usuario
        )
        return redirect('index')
    return render(request, 'solicitar_trueque.html', {
        'libro_deseado': libro_deseado,
        'mis_libros': mis_libros
    })
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
