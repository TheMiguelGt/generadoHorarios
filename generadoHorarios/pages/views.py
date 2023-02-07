from multiprocessing import context
from pydoc import render_doc
from re import search
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic.list import ListView #crear una lista de paginas
from django.views.generic.detail import DetailView #detalles de la pagina, solo para lectura
from django.views.generic.edit import CreateView,UpdateView,DeleteView #crear nuevas vistas,actualizar y eliminar 
from django.contrib.admin.views.decorators import staff_member_required #personas del staff
from django.utils.decorators import method_decorator #usar como decorador sus funciones
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from itertools import chain
from operator import attrgetter
from .models import Disponibilidad, Page,DocenteMateria,Dia,Hora
from usuarios.models import Admin,Coordina,Docente
from institucion.models import Aula,Semestre
from .forms import PageForms,DoceMateForms,DispoForms,DiaForms,HoraForms
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from institucion.views import StaffRequiredMixin,StaffCoordinaRequiredMixin

# Create your views here.
@login_required(login_url="usuarios:login")   
def pageListSearch(request):
    if request.method =='POST':
        searched = request.POST['searched']
        page_Search = Page.objects.filter(Q(clave__icontains=searched) | Q(materia__icontains=searched))
        page_obj = Page.history.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        # Paginate historical
        paginator = Paginator(page_obj,3)
        page = request.GET.get('pages')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
            
        # Paginate pages
        paginator1 = Paginator(page_Search,5)
        page1 = request.GET.get('pages:pages')
        try:
            page_Search = paginator1.page(page1)
        except PageNotAnInteger:
            page_Search = paginator1.page(1)
        except EmptyPage:
            page_Search = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/page_list_search.html',{'searched':searched,'page_Search':page_Search,'page_obj':page_obj,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        page_obj = Page.history.all()    
        pages = Page.objects.all()
        page_Search = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        # Paginate historical
        paginator = Paginator(page_obj,3)
        page = request.GET.get('pages')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
            
        # Paginate pages
        paginator1 = Paginator(page_Search,5)
        page1 = request.GET.get('pages:pages')
        try:
            page_Search = paginator1.page(page1)
        except PageNotAnInteger:
            page_Search = paginator1.page(1)
        except EmptyPage:
            page_Search = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/page_list_search.html',{'page_Search':page_Search,'page_obj':page_obj,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    
class PageDetailView(LoginRequiredMixin, DetailView):#ver detalles
    model = Page
    redirect_field_name = "usuarios:login"

# @method_decorator(staff_member_required,name='dispatch')
class PageCreate(LoginRequiredMixin,StaffCoordinaRequiredMixin,CreateView):#crear
    model = Page
    form_class = PageForms #se pasa la clase que se creo 
    success_url = reverse_lazy('pages:pages') #se puede hacer de dos maneras 
    template_name = 'pages/page_form.html'
    success_message = "Materia creada con exito"
    redirect_field_name = "usuarios:login"

    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        context['history_list'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        context['aul'] = Aula.objects.all()
        context['action'] = 'add'
        context['list_url'] = '/mate/materia/'
        
        return context

# @method_decorator(staff_member_required,name='dispatch')
class PageUpdate(LoginRequiredMixin,StaffCoordinaRequiredMixin,UpdateView):
    model = Page
    form_class = PageForms #campos para actualizar
    template_name_suffix = '_update_form' #se pasa un subfijo para usar otro formulario
    success_message = "Materia editada con exito"
    success_url = reverse_lazy('pages:pages')
    redirect_field_name = "usuarios:login"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['history_list'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        context['aul'] = Aula.objects.all()
        return context

    def get_success_url(self): #mostrar el formulario para ver los cambios
        success_url = reverse_lazy('pages:pages')
        # return reverse_lazy('pages:pages', args=[self.object.id]) + '?ok' #se recrea la url, donde se le pasa el update y la clave primaria con el indicador 
        return success_url

# @method_decorator(staff_member_required,name='dispatch')
class PageDelete(LoginRequiredMixin,StaffCoordinaRequiredMixin,DeleteView):#eliminar
    model = Page 
    success_url = reverse_lazy('pages:pages')
    success_message = "Materia eliminada con exito"
    redirect_field_name = "usuarios:login"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['history_list'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
#create docente materia
@login_required(login_url="usuarios:login")
def DoceMateListView(request):#listar
    if request.method =='POST':
        searched = request.POST['searched']
        matedo = DocenteMateria.objects.all()
        model = DocenteMateria.objects.filter(Q(materia__materia__icontains=searched) | Q(materia__clave__icontains=searched) | Q(docente__nombre__icontains=searched))   #se obtiene el modelo de la app
        histo = DocenteMateria.history.select_related('materia','docente')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        mate = Page.objects.all()
        doce = Docente.objects.all()
        seme = Semestre.objects.all()
        
        if not seme:
            messages.warning(request,'No hay horarios creados, favor de crear uno')
            return redirect('homeUser')
        elif not doce and request.user.is_staff or not doce and request.user.is_admin or not doce and request.user.is_coordina :
            messages.warning(request,'No hay docentes creados, favor de crear uno')
            return redirect('usuarios:DocenteSignUp')
        elif not mate:
            messages.warning(request,'No hay materias creadas, favor de crear una')
            return redirect('pages:pages')
        else:
            #Paginate historical 
            paginator = Paginator(histo,3)
            page = request.GET.get('pages')
            try:
                histo = paginator.page(page)
            except PageNotAnInteger:
                histo = paginator.page(1)
            except EmptyPage:
                histo = paginator.page(paginator.num_pages)
                
            #Paginate docemates
            paginator1 = Paginator(model,5)
            page1 = request.GET.get('pages:docemates')
            try:
                model = paginator1.page(page1)
            except PageNotAnInteger:
                model = paginator1.page(1)
            except EmptyPage:
                model = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/docentemateria_list.html',{'searched':searched,'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'histo':histo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        model = DocenteMateria.objects.all()
        histo = DocenteMateria.history.select_related('materia','docente')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        mate = Page.objects.all()
        doce = Docente.objects.all()
        seme = Semestre.objects.all()
        
        if not seme:
            messages.warning(request,'No hay horarios creados, favor de crear uno')
            return redirect('homeUser')
        elif not doce and request.user.is_staff or not doce and request.user.is_admin or not doce and request.user.is_coordina :
            messages.warning(request,'No hay docentes creados, favor de crear uno')
            return redirect('usuarios:DocenteSignUp')
        elif not mate:
            messages.warning(request,'No hay materias creadas, favor de crear una')
            return redirect('pages:pages')
        else:
            #Paginate historical 
            paginator = Paginator(histo,3)
            page = request.GET.get('pages')
            try:
                histo = paginator.page(page)
            except PageNotAnInteger:
                histo = paginator.page(1)
            except EmptyPage:
                histo = paginator.page(paginator.num_pages)
                
            #Paginate docemates
            paginator1 = Paginator(model,5)
            page1 = request.GET.get('pages:docemates')
            try:
                model = paginator1.page(page1)
            except PageNotAnInteger:
                model = paginator1.page(1)
            except EmptyPage:
                model = paginator1.page(paginator1.num_pages)
            #Paginate historical 
            paginator = Paginator(histo,3)
            page = request.GET.get('pages')
            try:
                histo = paginator.page(page)
            except PageNotAnInteger:
                histo = paginator.page(1)
            except EmptyPage:
                histo = paginator.page(paginator.num_pages)
                
            #Paginate docemates
            paginator1 = Paginator(model,5)
            page1 = request.GET.get('pages:docemates')
            try:
                model = paginator1.page(page1)
            except PageNotAnInteger:
                model = paginator1.page(1)
            except EmptyPage:
                model = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/docentemateria_list.html',{'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'histo':histo,'admin':admin,'coordina':coordina,'docente':docente})

class DoceMateDetail(LoginRequiredMixin,DetailView):
    model = DocenteMateria
    redirect_field_name = "usuarios:login"

class DoceMateCreate(LoginRequiredMixin,CreateView):
    model = DocenteMateria
    form_class = DoceMateForms
    success_url = reverse_lazy('pages:docemates')
    success_message = "Materia asignada se ha creado con exito"
    redirect_field_name = "usuarios:login"

    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        context['history_list'] = DocenteMateria.history.select_related('materia','docente')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        context['action'] = 'add'
        context['list_url'] = '/mate/materia/'
        
        return context
    
class DoceMateUpdate(LoginRequiredMixin,UpdateView):
    model = DocenteMateria
    form_class = DoceMateForms
    template_name_suffix = '_update_form'
    success_message = "Materia asignada se ha editado con exito"
    redirect_field_name = "usuarios:login"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = DocenteMateria.history.select_related('materia','docente')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context 
    
    def get_success_url(self):
        return reverse_lazy('pages:docemates')

class DoceMateDelete(LoginRequiredMixin ,DeleteView):
    model = DocenteMateria
    success_url = reverse_lazy('pages:docemates')
    success_message = "Materia asignada se ha eliminado con exito"
    redirect_field_name = "usuarios:login"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = DocenteMateria.history.select_related('materia','docente')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context 
    
#Disponibilidad de horario docente
@login_required(login_url="usuarios:login")    
def dispoListSearch(request):

    if request.method =="POST":
        searched = request.POST['searched']
        model = Disponibilidad.objects.all()
        disdo = Disponibilidad.objects.filter(Q(docente__nombre__icontains=searched) )
        history_list = Disponibilidad.history.select_related('docente','dia','horaini','horafin')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        #Paginate historical 
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages:disponi')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page('pages:disponi') 
            
        #Paginate disponi
        paginator1 = Paginator(disdo,5)
        page1 = request.GET.get('pages:disponi')
        try:
            disdo = paginator1.page(page1)
        except PageNotAnInteger:
            disdo = paginator1.page(1)
        except EmptyPage:
            disdo = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/disponibilidad_list.html',{'searched':searched,'disdo':disdo,'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        disdo = Disponibilidad.objects.all()
        history_list = Disponibilidad.history.select_related('docente','dia')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        #Paginate historical 
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages:disponi')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page(paginator.num_pages)
            
        #Paginate disponi
        paginator1 = Paginator(disdo,5)
        page1 = request.GET.get('pages:disponi')
        try:
            disdo = paginator1.page(page1)
        except PageNotAnInteger:
            disdo = paginator1.page(1)
        except EmptyPage:
            disdo = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/disponibilidad_list.html',{'disdo':disdo,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    
class DispoCreate(LoginRequiredMixin,CreateView):
    model = Disponibilidad
    form_class = DispoForms
    success_url = reverse_lazy('pages:disponi')
    redirect_field_name = "usuarios:login"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Disponibilidad.history.select_related('docente','dia','hora')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
class DispoUpdate(LoginRequiredMixin,UpdateView):
    model = Disponibilidad
    form_class = DispoForms
    template_name_suffix = '_update_form'
    redirect_field_name = "usuarios:login"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Disponibilidad.history.select_related('docente','dia','hora')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
    def get_success_url(self):
        return reverse_lazy('pages:dispoupdate',args=[self.object.id]) + '?ok'

class DispoDelete(LoginRequiredMixin,DeleteView):
    model = Disponibilidad
    success_url = reverse_lazy('pages:disponi')
    redirect_field_name = "usuarios:login"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Disponibilidad.history.select_related('docente','dia','hora')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

#Horario
def AlumnoSignUp(request):
    user_type = 'alumno'
    registered = False
    return render(request,'mate/horario.html')