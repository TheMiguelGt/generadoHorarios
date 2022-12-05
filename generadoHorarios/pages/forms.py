from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Page,DocenteMateria,Disponibilidad,Dia,Hora

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['clave','materia','carga']
        widgets  = {
            'clave': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Clave materia'}), #se a�aden los atributos y se le pone la clase o id para modificar
            'materia': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Nombre de la materia'}),
            'carga': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Numero de horas'}),
            
        }
        labels = {
            'clave':'Clave', 'materia':'Nombre','carga':'Numero horas'#,'idDoce':''
        }

class DoceMateForms(forms.ModelForm):
    class Meta:
        model = DocenteMateria
        fields = ['materia','docente','aula']
        
class DispoForms(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['docente','dia','hora']
        
class DiaForms(forms.ModelForm):
    class Meta:
        model = Dia
        fields = ['dia']
        
class HoraForms(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ['iniHora','finHora']