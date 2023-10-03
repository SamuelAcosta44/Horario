from django import forms
from .models import Tarea, Materia


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'materia', 'fecha_entrega']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
        }

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'profesor', 'dia', 'hora']
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'})
        }
        