from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Pelicula
from .forms import PeliculaForm
from datetime import datetime

# Create your views here.
def home(request):
    peliculas = Pelicula.objects.all()
    if request.user.is_authenticated:
        return render(request, "home.html", {'peliculas': peliculas, 'usuario': request.user})
    else:
        return render(request, "home.html", {'peliculas': peliculas})


def horarios(request, id):
    pelicula = Pelicula.objects.get(id=id)

    return render(request, 'horarios.html', {'pelicula': pelicula})

def search(request):
    if request.method == 'POST':
        fecha = request.POST['fecha']
        fecha_tipo = datetime.strptime(fecha, '%Y-%m-%d')

        peliculas = Pelicula.objects.filter(fecha_estreno=fecha_tipo)

        return render(request, "search.html", {'peliculas': peliculas})
    else:
        return redirect('home')


def iniciar_sesion(request):
    peliculas = Pelicula.objects.all()
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        contrasena = request.POST['contrasena']
        usuario = authenticate(request, username=nombre_usuario, password=contrasena)

        if usuario is not None:
            login(request, usuario)
            request.__setattr__('usuario', usuario)
            return redirect('home')
        else:
            return render(request, 'home.html', {'error': "Usuario no encontrado",
                                                 'peliculas': peliculas})
    else:
        return render(request, 'login.html')

def peliculas(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formulario = PeliculaForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return render(request, 'peliculas.html',
                              {'formulario': formulario, 'mensaje': 'Pelicula almacenada'})
        else:
            formulario = PeliculaForm()
            return render(request, 'peliculas.html', {'formulario': formulario})
    else:
        return redirect('login')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')
