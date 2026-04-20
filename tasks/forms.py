from .models import Task
from django import forms

class TaskForm(forms.ModelForm): 
    class Meta:
        model= Task
        fields= ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese titulo de la tarea...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese descripción de la tarea...'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
    
        