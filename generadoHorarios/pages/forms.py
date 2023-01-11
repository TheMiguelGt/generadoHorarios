from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Page,DocenteMateria,Disponibilidad,Dia,Hora

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = '__all__'

class DoceMateForms(forms.ModelForm):
    class Meta:
        model = DocenteMateria
        fields = '__all__'
        
class DispoForms(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['docente','dia','horaini','horafin','semestre','licenciatura']
        
class DiaForms(forms.ModelForm):
    class Meta:
        model = Dia
        fields = ['dia']
        
class HoraForms(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ['iniHora','finHora']