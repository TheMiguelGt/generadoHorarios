from asyncore import write
from atexit import register
from http.client import responses
import imp
from multiprocessing import connection, context
import profile
from unittest import result
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
from .models import User,Admin,Coordina,Docente,Alumno
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt
from pages.models import Dia,Hora,Disponibilidad,Page,DocenteMateria
from .resources import CoordinaResources,DocenteResources
from django.db.models import Count,Max
import csv,datetime
from tablib import Dataset
from usuarios import models
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password #mostrar o encryptar password



# Create your views here.
# ------------ PERFIL DE USUARIO ---------------
@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "usuarios/profile_view.html"
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

# ----------------Horario------------------
#tabla del horario
def horarioEsc(request):
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    dias = Dia.objects.all().order_by('id').distinct()
    print(dias.query)
    horas = Hora.objects.all().order_by('id').distinct()
    print(horas.query)
    pubs = Disponibilidad.objects.select_related('dia','hora','docente').annotate(tot=Count('hora')).order_by('hora__id','dia__id')
    print(pubs.query)
    context = {
        'admin':admin,
        'coordina':coordina,
        'docente':docente,
        'dias':dias,
        'horas':horas,
        'pubs':pubs,
    }
    return render(request,'usuarios/horario.html',context)

def export_csv(request):
    response =HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Horario'+\
        str(datetime.datetime.now())+'.csv'
    
    # dias = Dia.objects.all().values()
    writer = csv.writer(response)
    writer.writerow(['Horario disponible','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'])
   
    horas = Hora.objects.all()
    for hora in horas:
        writer.writerow([hora.iniHora+" - "+hora.finHora])
    
    return response

# ----------------ADMINISTRADOR------------------
#creation user admin
def AdminSignUp(request):
    user_type = 'administrador'
    registered = False
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    
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
            
            messages.success(request, "Administrador creado con exito")
            return HttpResponseRedirect(reverse('usuarios:administradores'))
    else:
        user_form = UserForm()
        admin_profile_form = AdminProfileForm()

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            data = Admin.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    return render(request,'usuarios/admin_signup.html',{'user_form':user_form,'admin_profile_form':admin_profile_form,'registered':registered,'user_type':user_type,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

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
        context = super(AdminListView,self).get_context_data(**kwargs)
        context['title'] = 'Listado de administradores'
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
@method_decorator(login_required, name="dispatch")
class AdminUpView(UpdateView):
    model = Admin
    fields = ['email','admin_profile_pic']
    success_url = reverse_lazy('usuarios:admin_update')
    template_name = "usuarios/admin_detail_page.html"
    
    def get_object(self):
        profile, created = Admin.objects.get_or_create(user=self.request.user)
        return profile
    
    def get_context_data(self, **kwargs):
        context = super(AdminUpView,self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
def adminList(request):
    if request.method == "POST":
        searched = request.POST['searched']
        adm = Admin.objects.filter(Q(user__username__icontains=searched) | Q(nombre__icontains=searched) | Q(apepat__icontains=searched) | Q(apemat__icontains=searched))
        model = Admin.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'usuarios/admin_list.html',{'searched':searched,'adm':adm,'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else: 
        model = Admin.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'usuarios/admin_list.html',{'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

class AdminDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "admin"
    model = models.Admin
    template_name = 'usuarios/admin_detail_page.html'


# ----------------COORDINADOR------------------

#creation profile coordina
def CoordinaSignUp(request):
    user_type = 'coordinador'
    registered = False
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    
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

            messages.success(request, "Coordinador creado con exito")
            return HttpResponseRedirect(reverse('usuarios:coordinadores'))
        else:
            print(user_form.errors,coordina_profile_form.errors)
    else:
        user_form = UserForm()
        coordina_profile_form = CoordinaProfileForm()
    
    return render(request,'usuarios/coordina_signup.html',{'user_form':user_form,'coordina_profile_form':coordina_profile_form,'registered':registered,'user_type':user_type,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

@method_decorator(login_required, name="dispatch")
class CoordinaUpView(UpdateView):
    model = Coordina
    fields = ['email','coordina_profile_pic']
    success_url = reverse_lazy('usuarios:coordina_profile')
    template_name = "usuarios/coordina_update.html"
    
    def get_object(self):
        profile, created = Coordina.objects.get_or_create(user=self.request.user)
        return profile
    
    def get_context_data(self, **kwargs):
        context = super(CoordinaUpView,self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

def coordina_upload(request):
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    
    if request.method == "POST":
        coordina_resource = CoordinaResources()
        dataset = Dataset()
        new_coordina = request.FILES['myfile']
        
        if not new_coordina.name.endswith('xlsx'):
            messages.info(request,'Error en el formato')
            return render(request,'usuarios/coordina_file.html')

        imported_data = dataset.load(new_coordina.read(),format='xlsx')
        for data in imported_data:
            value = User(
                data[0],
                make_password(data[1]),
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
            )
            value2 = Coordina(
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
            )
            value.save()
            value2.save()
    return render(request,'usuarios/coordina_file.html',{'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

#list all corrdinators users
class CoordinaListView(ListView):
    model = Coordina
    paginate_by=8

def coordinaList(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cor = Coordina.objects.filter(Q(user__username__icontains=searched) | Q(nombre__icontains=searched) | Q(apepat__icontains=searched) | Q(apemat__icontains=searched))
        model = Coordina.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'usuarios/coordina_list.html',{'searched':searched,'cor':cor,'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        model = Coordina.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'usuarios/coordina_list.html',{'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

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
    
    def get_context_data(self, **kwargs):
        context = super(CoordinaDelete,self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

#docente profile coordina
def DocenteSignUp(request):
    user_type = 'docente'
    registered = False
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    
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

            messages.success(request, "Docente creado con exito")
            return HttpResponseRedirect(reverse('usuarios:docentes'))
    else:
        user_form = UserForm()
        docente_profile_form = DocenteProfileForm()
    
    return render(request,'usuarios/docente_signup.html',{'user_form':user_form,'docente_profile_form':docente_profile_form,'registered':registered,'user_type':user_type,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

def docente_upload(request):
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    
    if request.method == "POST":
        docente_resource = DocenteResources()
        dataset = Dataset() #acceder a los datos del archivo
        new_docente = request.FILES['myfile'] #nombre del input file
        
        if not new_docente.endswith('xlsx'):
            messages.info(request,'Error en el formato')
            return render(request,'usuarios/docente_file.html')
        
        imported_data = dataset.load(new_docente.read(),format='xlsx')
        for data in imported_data:
            value = User(
                data[0],
                make_password(data[1]),
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
            )
            value2 = Docente(
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
            )
            value.save()
            value2.save()
    return render(request,'usuarios/docente_file.html',{'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

#list all docente users
class DocenteListView(ListView):
    model = Docente
    #paginate_by=8

def docenteList(request):
    if request.method == "POST":
        searched = request.POST['searched']
        doc = Docente.objects.filter(Q(user__username__icontains=searched) | Q(nombre__icontains=searched) | Q(apepat__icontains=searched) | Q(apemat__icontains=searched))
        model = Docente.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'usuarios/docente_list.html',{'searched':searched,'doc':doc,'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        model = Docente.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'usuarios/docente_list.html',{'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})

#docente profile coordina
def AlumnoSignUp(request):
    user_type = 'alumno'
    registered = False
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    
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
    
    return render(request,'usuarios/alumno_signup.html',{'user_form':user_form,'alumno_profile_form':alumno_profile_form,'registered':registered,'user_type':user_type,'pages':pages,'disponi':disponi,'matedo':matedo})

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
        
