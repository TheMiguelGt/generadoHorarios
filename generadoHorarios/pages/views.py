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
from .forms import PageForms,DoceMateForms,DispoForms
from django.core.paginator import Paginator
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
        return render(request,'pages/page_list_search.html',{'searched':searched,'page_Search':page_Search,'page_obj':page_obj,'pages':pages,'disponi':disponi,'matedo':matedo})
    else:
        page_obj = Page.history.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        paginator = Paginator(pages,8)
        
        page_number = request.GET.get('pages')
        owo_list = paginator.get_page(page_number)
        return render(request,'pages/page_list_search.html',{'page_obj':page_obj,'pages':pages,'disponi':disponi,'matedo':matedo,'owo_list':owo_list})
    
class PageDetailView(DetailView):#ver detalles
    model = Page

# @method_decorator(staff_member_required,name='dispatch')
class PageCreate(SuccessMessageMixin, CreateView):#crear
    model = Page
    form_class = PageForms #se pasa la clase que se creo 
    success_url = reverse_lazy('pages:pages') #se puede hacer de dos maneras 
    template_name = 'pages/page_form.html'
    success_message = "Materia creada con exito"
    
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                forms = self.get_form()
                if forms.is_valid():
                    forms.save()
                else:
                    data['error'] = forms.errors
            else:
                data['error'] = 'No ha ingresado ningun dato'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        context['history_list'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['action'] = 'add'
        context['list_url'] = '/mate/materia/'
        
        return context

# @method_decorator(staff_member_required,name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForms #campos para actualizar
    template_name_suffix = '_update_form' #se pasa un subfijo para usar otro formulario

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['history_list'] = Page.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        return context

    def get_success_url(self): #mostrar el formulario para ver los cambios
        # success_url = reverse_lazy('pages:pages')
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok' #se recrea la url, donde se le pasa el update y la clave primaria con el indicador 

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
        matedo = DocenteMateria.objects.all()
        return render(request,'pages/docentemateria_list.html',{'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'histo':histo})
    else:
        model = DocenteMateria.objects.all()
        histo = DocenteMateria.history.select_related('materia','docente')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        paginator = Paginator(histo,3)
        
        page_number = request.GET.get('docemates')
        page_obj = paginator.get_page(page_number)
        return render(request,'pages/docentemateria_list.html',{'page_obj':page_obj,'model':model,'pages':pages,'disponi':disponi,'matedo':matedo,'histo':histo})
    # paginate_by = 8 #paginacion de la lista, para mostrar de 3 en 3

class DoceMateDetail(DetailView):
    model = DocenteMateria

class DoceMateCreate(CreateView):
    model = DocenteMateria
    form_class = DoceMateForms
    success_url = reverse_lazy('pages:docemates')

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        return context
    
    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        context['history_list'] = DocenteMateria.history.select_related('materia','docente')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
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
        return context 
    
    def get_success_url(self):
        return reverse_lazy('pages:doceupdate',args=[self.object.id]) + '?ok'

class DoceMateDelete(DeleteView):
    model = DocenteMateria
    success_url = reverse_lazy('pages:docemates')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = DocenteMateria.history.select_related('materia','docente')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
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
        return context
    
def dispoListSearch(request):
    if request.method =="POST":
        searched = request.POST['searched']
        model = Disponibilidad.objects.all()
        disdo = Disponibilidad.objects.filter(Q(docente__nombre__icontains=searched) )
        history_list = Disponibilidad.history.select_related('docente','dia','hora')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        return render(request,'pages/disponibilidad_list.html',{'disdo':disdo,'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo})
    else:
        model = Disponibilidad.objects.all()
        history_list = Disponibilidad.history.select_related('docente','dia','hora')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        return render(request,'pages/disponibilidad_list.html',{'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo})
    
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
        return context
    

#Horario
def AlumnoSignUp(request):
    user_type = 'alumno'
    registered = False
    return render(request,'mate/horario.html')