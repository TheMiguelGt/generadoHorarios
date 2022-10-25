from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Plantel

class PlantelForms(forms.ModelForm):
    class Meta:
        model = Plantel
        fields = ['clave','plantel']
        widget = {
            'clave': forms.TextInput(attrs={'placeholder':'Clave del plantel'}),
            'plantel': forms.TextInput(attrs={'placeholder':'Nombre del plantel'}),
        }
        