import imp
from django.shortcuts import render,get_list_or_404,redirect
from django.views import generic
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm,AdminProfileForm,CoordinaProfileForm,DocenteProfileForm,AlumnoProfileForm,AdminProfileIUpdateForm,CoordinaProfileIUpdateForm,DocenteProfileIUpdateForm,AlumnoProfileIUpdateForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from .models import Admin,Coordina,Docente,Alumno
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
#creation profile coordina
def CoordinaSignUp(request):
    user_type = 'coordinador'
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        coordina_profile_form = CoordinaProfileForm(data = request.POST)
        
        if user_form.is_valid() and coordina_profile_form.is_valid():
            user = user_form.save()
            user.is_coordina = True
            user.save()
            
            profile = coordina_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
        else:
            print(user_form.errors,coordina_profile_form.errors)
    else:
        user_form = UserForm()
        coordina_profile_form = CoordinaProfileForm()
    
    return render(request,'usuarios/coordina_signup.html',{'user_form':user_form,'coordina_profile_form':coordina_profile_form,'registered':registered,'user_type':user_type})

#login view
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('homeUser'))
            else:
                return HttpResponse("Cuenta no activa")
        else:
            messages.error(request, "Detalles invalidos")
            return redirect('usuarios:login')
    else:
        return render(request,'usuarios/login.html',{})

#logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
        