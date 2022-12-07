from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms 
from .models import Plantel,Licenciatura,Aula,Semestre,Ciclo

class PlantelForms(forms.ModelForm):
    class Meta:
        model = Plantel
        fields = ['clave','plantel']
        widget = {
            'clave': forms.TextInput(attrs={'placeholder':'Clave del plantel'}),
            'plantel': forms.TextInput(attrs={'placeholder':'Nombre del plantel'}),
        }
        
PLANTEL_CHOICES = [
    ('Select','Select'),
    Plantel.objects,]

class LicenciaturaForms(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = ['clave','licenciatura','plantel']
        widget = {
            'clave': forms.TextInput(attrs={'placeholder':'Clave de la licenciatura','class':"txt-all"}),
            'licenciatura': forms.TextInput(attrs={'placeholder':'Nombre de la licenciatura'}),
            'plantel': forms.RadioSelect(attrs={'class': "txt-all"}),
        }

class AulaForms(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['clave','piso','plantel']
        
class SemestreForms(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['semestre','licenciatura']
        
class CicloForms(forms.ModelForm):
    class Meta:
        model = Ciclo
        fields = ['ciclo']