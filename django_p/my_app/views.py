from django.shortcuts import render, redirect
from .forms import TareaForm, MateriaForm
from .models import Materia, Tarea

# Create your views here.


def home(request):
    if request.method == 'GET':
        materia = Materia.objects.all()
        return render(request, 'home.html', {
            'materias': materia
        })


def agregar_tarea(request):
    return render(request, 'agregar_tarea.html', {
        'form': TareaForm()
    })


def agregar_materia(request):
    if request.method == 'GET':
        return render(request, 'agregar_materia.html', {
            'form': MateriaForm()
        })
    else:
        try:
            materia = MateriaForm(request.POST)
            materia.save()
            return redirect('home')
        except:
            return redirect('home')