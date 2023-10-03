from django.urls import path
from .views import home, agregar_tarea, agregar_materia

urlpatterns = [
    path('home/', home, name='home'),
    path('tarea/agregar/', agregar_tarea, name='agregar_tarea'),
    path('materia/agregar/', agregar_materia, name='agregar_materia'),
]
