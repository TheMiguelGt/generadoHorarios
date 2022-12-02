from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from multiprocessing import context
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from pages.models import Page,Disponibilidad,DocenteMateria
from django.core.paginator import Paginator
from usuarios.models import Admin,Coordina,Docente
from institucion.models import Plantel

# Create your views here.
class HomePageView(TemplateView): #se crea una clase para poder hacer la vista del home
    template_name = 'core/home.html'
    #se obtiene la ruta por medio de la variable 
    def get(self, request, *args, **kwargs):#importante traer los argumentos y clave valor
        return render(request,self.template_name,{'title':'Home'})


class HomeUserView(TemplateView): #se crea una clase para poder hacer la vista del home
    template_name = 'core/homeuser.html'
    #se obtiene la ruta por medio de la variable 
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):#importante traer los argumentos y clave valor
        return render(request,self.template_name,{'title':'UserView'})
    
    def get_context_data(self, **kwargs):
        context = super(HomeUserView, self).get_context_data(**kwargs)
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

def homePage2View(request):
    histo = Page.history.all()
    paginator = Paginator(histo,3)
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    
    print(pages.query)
    page_number = request.GET.get('homeUser')
    page_obj = paginator.get_page(page_number)
    return render(request,'core/home2.html',{'page_obj': page_obj,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    
class UserPageView(TemplateView):
    template_name = 'core/userhome1.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):#importante traer los argumentos y clave valor
        return render(request,self.template_name,{'title':'userPage'})
    
    def get_context_data(self, **kwargs):
        context = super(UserPageView, self).get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    

    