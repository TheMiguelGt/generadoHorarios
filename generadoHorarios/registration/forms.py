from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Profile

# class UserCreationFormWithEmail(UserCreationForm):
#     email = forms.EmailField(required=True,help_text="Requerido, 254 caracteres como maximo y debe ser valido")

#     class Meta:
#         model = User 
#         fields = ("username","email","password1","password2")

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("El email ya está registrado, prueba con otro.")
#         return email

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['avatar']
#         widgets = {
#             'avatar': forms.ClearableFileInput,
#         }