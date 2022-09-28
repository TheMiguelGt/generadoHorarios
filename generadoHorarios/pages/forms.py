from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Page

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['idMateria','nomMateria','numHoras','aula','grado']
        Widget = {
            'idMateria': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Id materia'}), #se a�aden los atributos y se le pone la clase o id para modificar
            'nomMateria': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Nombre de la materia'}),
            'numHoras': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Numero de horas'}),
            'grado': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Grado'}),
            'aula': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Aula'}),
            
        }
        labels = {
            'idMateria':'Clave de la materia', 'nomMateria':'Nombre de la materia','numHoras':'Numero de horas','aula':'Aula','grado':'grado'#,'idDoce':''
        }