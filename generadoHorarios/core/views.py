from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from multiprocessing import context
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

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

class HomePage2View(TemplateView):
    template_name = 'core/home2.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):#importante traer los argumentos y clave valor
        return render(request,self.template_name,{'title':'homeUser'})

    