from django.views.generic.list import ListView #crear una lista de paginas
from django.views.generic.detail import DetailView #detalles de la pagina
from .models import Page

# Create your views here.
class PageListView(ListView):
    model = Page    #se obtiene el modelo de la app

class PageDetailView(DetailView):
    model = Page