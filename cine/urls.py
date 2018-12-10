from django.urls import path
from .views import home, horarios, search, peliculas, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('', home, name='home'),
    # path('home/<usuario>', home, name='home'),
    path('horarios/<id>', horarios, name='horarios'),
    path('search/', search, name='search'),
    path('peliculas/', peliculas, name='peliculas'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout')
]