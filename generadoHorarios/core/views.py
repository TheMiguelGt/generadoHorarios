from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from multiprocessing import context
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from pages.models import Page,Disponibilidad,DocenteMateria
from django.core.paginator import Paginator
from usuarios.models import Admin,Coordina,Docente
from institucion.models import Plantel,Semestre
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

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
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        seme = Semestre.objects.filter(Q(semestre__icontains=searched) | Q(licenciatura__licenciatura__icontains=searched))
        history_list = Semestre.history.select_related('licenciatura')
        model = Semestre.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        
        #Paginate historical
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page(paginator.num_pages)
            
        #Paginate horarios
        paginator1 = Paginator(seme,5)
        page1 = request.GET.get('homeUser')
        try:
            seme = paginator1.page(page1)
        except PageNotAnInteger:
            seme = paginator1.page(1)
        except EmptyPage:
            seme = paginator1.page(paginator1.num_pages)
        
        return render(request,'institucion/semestre_list.html',{'searched':searched,'seme':seme,'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        history_list = Semestre.history.select_related('licenciatura')
        model = Semestre.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        
        #Paginate historical
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page(paginator.num_pages)
            
        #Paginate horarios
        paginator1 = Paginator(model,5)
        page1 = request.GET.get('homeUser')
        try:
            model = paginator1.page(page1)
        except PageNotAnInteger:
            model = paginator1.page(1)
        except EmptyPage:
            model = paginator1.page(paginator1.num_pages)
        
        return render(request,'institucion/semestre_list.html',{'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    
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
    

    