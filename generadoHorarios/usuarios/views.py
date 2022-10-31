from atexit import register
import imp
from multiprocessing import context
import profile
from urllib import request
from django import dispatch
from django.shortcuts import render,get_list_or_404,redirect
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import View,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from pages.models import Dia
from .forms import UserForm,AdminProfileForm,CoordinaProfileForm,DocenteProfileForm,AlumnoProfileForm,AdminProfileIUpdateForm,CoordinaProfileIUpdateForm,DocenteProfileIUpdateForm,AlumnoProfileIUpdateForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from .models import History, User,Admin,Coordina,Docente,Alumno
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt
from pages.models import Dia,Hora,Disponibilidad
# from tablib import Dataset
# from .resources import AdminResource


# Create your views here.

# ----------------Horario------------------
#tabla del horario
def horarioEsc(request):
    dias = Dia.objects.all().values()
    horas = Hora.objects.all().values()
    dispo = Disponibilidad.objects.all().values()
    context = {
        'dias':dias,
        'horas':horas,
        'dispo':dispo,
    }
    return render(request,'usuarios/horario.html',context)

# ----------------ADMINISTRADOR------------------
#creation user admin
def AdminSignUp(request):
    user_type = 'administrador'
    registered = False
    url = reverse('usuarios:administradores')

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            data = Admin.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        admin_profile_form = AdminProfileForm(data = request.POST)

        if user_form.is_valid() and admin_profile_form.is_valid():
            user = user_form.save()
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save()

            profile = admin_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            
            return HttpResponseRedirect(url)
    else:
        user_form = UserForm()
        admin_profile_form = AdminProfileForm()
    
    return render(request,'usuarios/admin_signup.html',{'user_form':user_form,'admin_profile_form':admin_profile_form,'registered':registered,'user_type':user_type})
    
# def importExcel(request):
#     user_type = 'administrador'
#     registered = False
#     url = reverse('usuarios:administradores')
    
#     if request.method == 'POST':
#         admin_resource = AdminResource()
#         dataset = Dataset()
#         new_admin = request.FILES['my_file']
#         imported_data = dataset.load(new_admin.read(),format='xlsx')
#         for data in imported_data:
#             value = Admin(
#                 data[0],
#                 data[4],
#                 data[5],
#                 data[6],
#                 data[7],
#             )
#             value.save()

#     return render(request,'usuarios/admin_import.html')

#Admin list view
class AdminListView(ListView):
    model = Admin
    paginate_by=8
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)    
    
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            data = Admin.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['title'] = 'Listado de administradores'
        return context

# ----------------COORDINADOR------------------

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

#list all corrdinators users
class CoordinaListView(ListView):
    model = Coordina
    #paginate_by=8

#delete coordinatior user
@method_decorator(login_required, name='dispatch')
class CoordinaDelete(DeleteView):
    model = User
    coordis = Coordina.objects.all().values()
    context = {
        'coordis':coordis,
    }
    success_url = reverse_lazy('usuarios:coordinadores',context)

    def dispatch(self,request,*args,**kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args,**kwargs)

#docente profile coordina
def DocenteSignUp(request):
    user_type = 'docente'
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        docente_profile_form = DocenteProfileForm(data = request.POST)
        
        if user_form.is_valid() and docente_profile_form.is_valid():
            user = user_form.save()
            user.is_docente = True
            user.save()
            
            profile = docente_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
        else:
            print(user_form.errors,docente_profile_form.errors)
    else:
        user_form = UserForm()
        docente_profile_form = DocenteProfileForm()
    
    return render(request,'usuarios/docente_signup.html',{'user_form':user_form,'docente_profile_form':docente_profile_form,'registered':registered,'user_type':user_type})

#list all docente users
class DocenteListView(ListView):
    model = Docente
    #paginate_by=8

#docente profile coordina
def AlumnoSignUp(request):
    user_type = 'alumno'
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        alumno_profile_form = AlumnoProfileForm(data = request.POST)
        
        if user_form.is_valid() and alumno_profile_form.is_valid():
            user = user_form.save()
            user.is_alumno = True
            user.save()
            
            profile = alumno_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
        else:
            print(user_form.errors,alumno_profile_form.errors)
    else:
        user_form = UserForm()
        alumno_profile_form = AlumnoProfileForm()
    
    return render(request,'usuarios/alumno_signup.html',{'user_form':user_form,'alumno_profile_form':alumno_profile_form,'registered':registered,'user_type':user_type})

#list all docente users
class AlumnoListView(ListView):
    model = Alumno
    #paginate_by=8


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
        
