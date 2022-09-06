from django.views.generic.list import ListView #crear una lista de paginas
from django.views.generic.detail import DetailView #detalles de la pagina
from django.views.generic.edit import CreateView #crear nuevas vistas
from django.urls import reverse, reverse_lazy
from .models import Page

# Create your views here.
class PageListView(ListView):#listar
    model = Page    #se obtiene el modelo de la app

class PageDetailView(DetailView):#ver detalles
    model = Page
    
class PageCreate(CreateView):#crear
    model = Page
    fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages') #se puede hacer de dos maneras 
    
    #def get_success_url(self): #metodo cuando se haya creado un nuevo horario, donde nos mandara al listado
     #   return reverse('pages:pages')
