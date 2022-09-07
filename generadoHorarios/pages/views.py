from django.views.generic.list import ListView #crear una lista de paginas
from django.views.generic.detail import DetailView #detalles de la pagina, solo para lectura
from django.views.generic.edit import CreateView,UpdateView,DeleteView #crear nuevas vistas,actualizar y eliminar 
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForms

# Create your views here.
class PageListView(ListView):#listar
    model = Page    #se obtiene el modelo de la app

class PageDetailView(DetailView):#ver detalles
    model = Page
    
class PageCreate(CreateView):#crear
    model = Page
    form_class = PageForms #se pasa la clase que se creo 
    success_url = reverse_lazy('pages:pages') #se puede hacer de dos maneras 
    #def get_success_url(self): #metodo cuando se haya creado un nuevo horario, donde nos mandara al listado
     #   return reverse('pages:pages')

class PageUpdate(UpdateView):
    model = Page
    form_class = PageForms #campos para actualizar
    template_name_suffix = '_update_form' #se pasa un subfijo para usar otro formulario

    def get_success_url(self): #mostrar el formulario para ver los cambios
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok' #se recrea la url, donde se le pasa el update y la clave primaria con el indicador 
    
class PageDelete(DeleteView):#eliminar
    model = Page 
    success_url = reverse_lazy('pages:pages')
    
