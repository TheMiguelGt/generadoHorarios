from multiprocessing import context
from pydoc import render_doc
from django.shortcuts import render
from django.http import JsonResponse
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

class StaffRequiredMixin(object): #clase base de todas las clases de py
    """El mixin requerira que sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs): #permitir controlar la peticion
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

# Create your views here.
def PageListView(request):#listar
    model = Page.objects.all()    #se obtiene el modelo de la app
    histo = Page.history.all()
    paginator = Paginator(histo,3)
    
    print(histo.query)
    print(model.query)
    page_number = request.GET.get('pages')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'pages/page_list.html',{'page_obj': page_obj,'model':model})
    

class PageDetailView(DetailView):#ver detalles
    model = Page

# @method_decorator(staff_member_required,name='dispatch')
class PageCreate( CreateView):#crear
    model = Page
    form_class = PageForms #se pasa la clase que se creo 
    success_url = reverse_lazy('pages:pages') #se puede hacer de dos maneras 
    #def get_success_url(self): #metodo cuando se haya creado un nuevo horario, donde nos mandara al listado
     #   return reverse('pages:pages')

# @method_decorator(staff_member_required,name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForms #campos para actualizar
    template_name_suffix = '_update_form' #se pasa un subfijo para usar otro formulario

    def get_success_url(self): #mostrar el formulario para ver los cambios
        # success_url = reverse_lazy('pages:pages')
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok' #se recrea la url, donde se le pasa el update y la clave primaria con el indicador 
    
# @method_decorator(staff_member_required,name='dispatch')
class PageDelete(DeleteView):#eliminar
    model = Page 
    success_url = reverse_lazy('pages:pages')
    
#create docente materia
class DoceMateListView(ListView):#listar
    model = DocenteMateria    #se obtiene el modelo de la app
    # paginate_by = 8 #paginacion de la lista, para mostrar de 3 en 3

class DoceMateCreate(CreateView):
    model = DocenteMateria
    form_class = DoceMateForms
    success_url = reverse_lazy('pages:docemates')
    
#Disponibilidad de horario docente
class DispoListView(ListView):
    model = Disponibilidad
    
    def get_queryset(self):
        dia = Dia.objects.all()
        return Disponibilidad.objects.all()
    # paginate_by = 8
    
class DispoCreate(CreateView):
    model = Disponibilidad
    form_class = DispoForms
    success_url = reverse_lazy('pages:disponi')

#Horario
def AlumnoSignUp(request):
    user_type = 'alumno'
    registered = False
    return render(request,'mate/horario.html')