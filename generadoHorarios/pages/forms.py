from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Page

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title','content','order']
        Widget = {
            'title': forms.TextInput(attrs={'class':'uwu-class','placeholder':'Titulo'}), #se añaden los atributos y se le pone la clase o id para modificar
            'content': forms.Textarea(attrs={'class':'uwu-class'}),
            'order': forms.NumberInput(attrs={'class':'uwu-class','placeholder':'Orden'}),
        }
        labels = {
            'title':'', 'order':'','content':''
        }