from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Plantel,Licenciatura

class PlantelForms(forms.ModelForm):
    class Meta:
        model = Plantel
        fields = ['clave','plantel']
        widget = {
            'clave': forms.TextInput(attrs={'placeholder':'Clave del plantel'}),
            'plantel': forms.TextInput(attrs={'placeholder':'Nombre del plantel'}),
        }
class LicenciaturaForms(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = ['clave','plantel','licenciatura']
        widget = {
            'clave': forms.TextInput(attrs={'placeholder':'Clave del plantel'}),
            'plantel': forms.TextInput(attrs={'placeholder':'Nombre del plantel'}),
            'licenciatura': forms.NumberInput(attrs={'placeholder':'Nombre del licenciatura'}),
        }