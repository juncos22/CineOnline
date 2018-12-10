from django.db import models
# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField("Nombre de la pelicula", max_length=100)
    genero = models.CharField("Genero de la pelicula", max_length=30)
    clasificacion = models.CharField("Clasificacion de la pelicula", max_length=1)
    duracion = models.PositiveIntegerField("Duracion en minutos")
    fecha_estreno = models.DateField("Fecha de estreno")
    horario = models.TimeField("Horarios disponibles")
    trailer = models.TextField("Trailer de la pelicula", default="N/A")
    portada = models.TextField("Portada de la pelicula")

class Usuario(models.Model):
    nombre_usuario = models.CharField("Nombre de usuario", max_length=10)
    contrasena = models.CharField("Contraseña", max_length=8)
    cargo = models.CharField("Cargo de usuario", max_length=20)
