from django.http import JsonResponse
from django.views.generic.list import ListView #crear una lista de paginas
from django.views.generic.detail import DetailView #detalles de la pagina, solo para lectura
from django.views.generic.edit import CreateView,UpdateView,DeleteView #crear nuevas vistas,actualizar y eliminar 
from django.contrib.admin.views.decorators import staff_member_required #personas del staff
from django.utils.decorators import method_decorator #usar como decorador sus funciones
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page,DocenteMateria
from .forms import PageForms

class StaffRequiredMixin(object): #clase base de todas las clases de py
    """El mixin requerira que sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs): #permitir controlar la peticion
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

# Create your views here.
class PageListView(ListView):#listar
    model = Page    #se obtiene el modelo de la app
    paginate_by = 8 #paginacion de la lista, para mostrar de 3 en 3

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
    paginate_by = 8 #paginacion de la lista, para mostrar de 3 en 3
