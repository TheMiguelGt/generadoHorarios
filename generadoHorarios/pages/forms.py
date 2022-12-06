from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Page,DocenteMateria,Disponibilidad,Dia,Hora

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['clave','materia','carga','grupo','aula']

class DoceMateForms(forms.ModelForm):
    class Meta:
        model = DocenteMateria
        fields = ['materia','docente','aula','semestre','licenciatura','ciclo']
        
class DispoForms(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['docente','dia','hora','semestre','licenciatura','ciclo']
        
class DiaForms(forms.ModelForm):
    class Meta:
        model = Dia
        fields = ['dia']
        
class HoraForms(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ['iniHora','finHora']