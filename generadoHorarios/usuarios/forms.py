from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Admin,Coordina,Docente,Alumno
from django.db import transaction

#user login form (applied other users)
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'txtform'}),
                'password1': forms.PasswordInput(attrs={'class':'txtform'}),
                'password2': forms.PasswordInput(attrs={'class':'txtform'}),
                }
        
#admins register form
class AdminProfileForm(forms.ModelForm):
    class Meta():
        model = Admin
        fields = ['nombre','apepat','apemat','email']
        widgets = {
                'nombre': forms.TextInput(attrs={'class':'txtform'}),
                'password1': forms.TextInput(attrs={'class':'txtform'}),
                'password2': forms.TextInput(attrs={'class':'txtform'}),
                }

#admin profile update
class AdminProfileIUpdateForm(forms.ModelForm):
    class Meta():
        model = Admin
        fields = ['email','admin_profile_pic']

#coordina register form
class CoordinaProfileForm(forms.ModelForm):
    class Meta():
        model = Coordina
        fields = ['nombre','apepat','apemat','email']
        widgets = {
                'nombre': forms.TextInput(attrs={'class':'txtform'}),
                'password1': forms.TextInput(attrs={'class':'txtform'}),
                'password2': forms.TextInput(attrs={'class':'txtform'}),
                }

#coordina profile update
class CoordinaProfileIUpdateForm(forms.ModelForm):
    class Meta():
        model = Coordina
        fields = ['email','coordina_profile_pic']

#docente register form
class DocenteProfileForm(forms.ModelForm):
    class Meta():
        model = Docente
        fields = ['nombre','apepat','apemat','email']
        widgets = {
                'nombre': forms.TextInput(attrs={'class':'txtform'}),
                'password1': forms.TextInput(attrs={'class':'txtform'}),
                'password2': forms.TextInput(attrs={'class':'txtform'}),
                }

#docente profile update
class DocenteProfileIUpdateForm(forms.ModelForm):
    class Meta():
        model = Docente
        fields = ['email','docente_profile_pic']

#alumno register form
class AlumnoProfileForm(forms.ModelForm):
    class Meta():
        model = Alumno
        fields = ['nombre','apepat','apemat','email']
        widgets = {
                'nombre': forms.TextInput(attrs={'class':'txtform'}),
                'password1': forms.TextInput(attrs={'class':'txtform'}),
                'password2': forms.TextInput(attrs={'class':'txtform'}),
                }

#alumno profile update
class AlumnoProfileIUpdateForm(forms.ModelForm):
    class Meta():
        model = Alumno
        fields = ['email','alumno_profile_pic']
