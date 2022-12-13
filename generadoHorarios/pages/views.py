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
from institucion.models import Aula
from .forms import PageForms,DoceMateForms,DispoForms,DiaForms,HoraForms
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

class StaffRequiredMixin(object): #clase base de todas las clases de py
    """El mixin requerira que sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs): #permitir controlar la peticion
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

# Create your views here.
class PageListView(ListView):#listar
    model = Page   #se obtiene el modelo de la app
    paginate_by = 8
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

    def post(self,request,*args,**kwargs):
        data = {}
        print(request.POST)
        if request.method == "POST":
            searched = request.POST['searched']
            return render(request,'pages/page_list.html',{'searched':searched})
        try:
            data = Page.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
   
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
    
class PageDetailView(DetailView):#ver detalles
    model = Page

# @method_decorator(staff_member_required,name='dispatch')
class PageCreate(SuccessMessageMixin, CreateView):#crear
    model = Page
    form_class = PageForms #se pasa la clase que se creo 
    success_url = reverse_lazy('pages:pages') #se puede hacer de dos maneras 
    template_name = 'pages/page_form.html'
    success_message = "Materia creada con exito"
    
    # def post(self,request,*args,**kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             forms = self.get_form()
    #             if forms.is_valid():
    #                 forms.save()
    #             else:
    #                 data['error'] = forms.errors
    #         else:
    #             data['error'] = 'No ha ingresado ningun dato'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

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
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForms #campos para actualizar
    template_name_suffix = '_update_form' #se pasa un subfijo para usar otro formulario
    success_url = reverse_lazy('pages:pages')

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
class PageDelete(DeleteView):#eliminar
    model = Page 
    success_url = reverse_lazy('pages:pages')

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

class DoceMateDetail(DetailView):
    model = DocenteMateria

class DoceMateCreate(CreateView):
    model = DocenteMateria
    form_class = DoceMateForms
    success_url = reverse_lazy('pages:docemates')

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
    
class DoceMateUpdate(UpdateView):
    model = DocenteMateria
    form_class = DoceMateForms
    template_name_suffix = '_update_form'
    
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

class DoceMateDelete(DeleteView):
    model = DocenteMateria
    success_url = reverse_lazy('pages:docemates')
    
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
class DispoListView(ListView):
    model = Disponibilidad
    paginate_by = 8
    
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
    
class DispoCreate(CreateView):
    model = Disponibilidad
    form_class = DispoForms
    success_url = reverse_lazy('pages:disponi')
    
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
    
class DispoUpdate(UpdateView):
    model = Disponibilidad
    form_class = DispoForms
    template_name_suffix = '_update_form'
    
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

class DispoDelete(DeleteView):
    model = Disponibilidad
    success_url = reverse_lazy('pages:disponi')
    
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
    
class DiaList(ListView):
    model = Dia
    paginate_by = 6 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
class DiaCreate(CreateView):
    model = Dia
    form_class = DiaForms
    success_url = reverse_lazy('pages:dias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        context['dia_nom'] = Dia.objects.all().order_by('dia')
        return context

class DiaUpdate(UpdateView):
    model = Dia
    form_class = DiaForms
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:dias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        context['dia_nom'] = Dia.objects.all().order_by('dia')
        return context
    
def HoraList(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        histo = DocenteMateria.history.select_related('materia','docente')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        horas =Hora.objects.all().order_by('iniHora','finHora').values()
        hora_li =Hora.objects.filter(Q(iniHora__icontains=searched) | Q(finHora__icontains=searched))
        
        #Paginate horas
        paginator1 = Paginator(hora_li,5)
        page1 = request.GET.get('pages:horas')
        try:
            hora_li = paginator1.page(page1)
        except PageNotAnInteger:
            hora_li = paginator1.page(1)
        except EmptyPage:
            hora_li = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/hora_list.html',{'searched':searched,'horas':horas,'hora_li':hora_li,'pages':pages,'disponi':disponi,'matedo':matedo,'histo':histo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        histo = DocenteMateria.history.select_related('materia','docente')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        horas =Hora.objects.all().order_by('iniHora','finHora').values()
        hora_li =Hora.objects.all().order_by('iniHora','finHora').values()
        
        #Paginate horas
        paginator1 = Paginator(hora_li,5)
        page1 = request.GET.get('pages:horas')
        try:
            hora_li = paginator1.page(page1)
        except PageNotAnInteger:
            hora_li = paginator1.page(1)
        except EmptyPage:
            hora_li = paginator1.page(paginator1.num_pages)
        
        return render(request,'pages/hora_list.html',{'hora_li':hora_li,'horas':horas,'pages':pages,'disponi':disponi,'matedo':matedo,'histo':histo,'admin':admin,'coordina':coordina,'docente':docente})

class HoraCreate(CreateView):
    model = Hora
    form_class = HoraForms
    success_url = reverse_lazy('pages:horas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
class HoraUpdate(UpdateView):
    model = Hora
    form_class = HoraForms
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:horas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = Page.history.all()
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