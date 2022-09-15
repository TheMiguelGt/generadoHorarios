from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get_success_url(self):#si fue con exito se le agrega algo al url
        return reverse_lazy('login')+'?register'

    def get_form(self,form_class=None):
        form = super(SignUpView,self).get_form()
        #modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Password'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Confirmar password'})
        
        return form

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['avatar','bio']
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        #recuperar el objeto que se editara
        profile, created = Profile.objects.get_or_create(user=self.request.user)#consigue o crea mediante el filtro
        return profile
