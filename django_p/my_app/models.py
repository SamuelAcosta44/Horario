from django.db import models
from datetime import time

# Create your models here.
class Materia(models.Model):
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
        ('Domingo', 'Domingo'),
    ]
    nombre = models.CharField(max_length=50)
    profesor = models.CharField(max_length=100)
    dia = models.CharField(max_length=10, choices=DIAS_SEMANA)
    hora = models.TimeField(default=time(6, 0))

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()