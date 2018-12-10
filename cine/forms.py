from django.forms import ModelForm
from .models import Pelicula, Usuario

class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = [
            'nombre',
            'genero',
            'clasificacion',
            'duracion',
            'fecha_estreno',
            'horario',
            'trailer',
            'portada'
        ]

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'contrasena',
            'cargo'
        ]
