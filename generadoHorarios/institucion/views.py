from django.urls import reverse_lazy
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from institucion.models import Aula, Plantel,Licenciatura, Semestre
from .forms import PlantelForms,LicenciaturaForms,AulaForms,SemestreForms
from pages.models import Page,Disponibilidad,DocenteMateria
from usuarios.models import Admin,Coordina,Docente
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q,Count
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages



# Create your views here.
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)

# START OF PLANTELES
class PlantelListView(ListView):
    model = Plantel
    paginate_by = 8
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        return context
    
def plantelList(request):
    if request.method == "POST":
        searched = request.POST['searched']
        plant = Plantel.objects.filter(Q(clave__icontains=searched) | Q(plantel__icontains=searched))
        history_list = Plantel.history.all()
        model = Plantel.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        #Paginate historical
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page(paginator.num_pages)
            
        #Paginate planteles
        paginator1 = Paginator(plant,5)
        page1 = request.GET.get('planteles:planteles')
        try:
            plant = paginator1.page(page1)
        except PageNotAnInteger:
            plant = paginator1.page(1)
        except EmptyPage:
            plant = paginator1.page(paginator1.num_pages)
        
        return render(request,'institucion/plantel_list.html',{'searched':searched,'plant':plant,'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        model = Plantel.objects.all()
        history_list = Plantel.history.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        #Paginate historical
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page(paginator.num_pages)
            
        #Paginate planteles
        paginator1 = Paginator(model,5)
        page1 = request.GET.get('planteles:planteles')
        try:
            model = paginator1.page(page1)
        except PageNotAnInteger:
            model = paginator1.page(1)
        except EmptyPage:
            model = paginator1.page(paginator1.num_pages)
            
        return render(request,'institucion/plantel_list.html',{'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
        
class PlantelDetailView(DetailView):
    model = Plantel
    
    def get_context_data(self, **kwargs):
        context = super(PlantelDetailView,self).get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

class PlantelCreate(CreateView):
    model = Plantel
    form_class = PlantelForms
    success_url = reverse_lazy('planteles:licenciaturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

class PlantelUpdate(UpdateView):
    model = Plantel
    form_class = PlantelForms
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
    def get_success_url(self):
        success_url = reverse_lazy('planteles:planteles')
        return success_url
    
class PlantelDelete(DeleteView):
    model = Plantel
    success_url = reverse_lazy('planteles:planteles')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
# END OF PLANTELES

# START OF LICENCIATURA
class LicenciaturaListView(ListView):
    model = Licenciatura

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Licenciatura.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
def licenciaturaList(request):
    if request.method == "POST":
        searched = request.POST['searched']
        model = Licenciatura.objects.all()
        licen = Licenciatura.objects.filter(Q(clave__icontains=searched) | Q(licenciatura__icontains=searched) | Q(plantel__plantel__icontains=searched))
        history_list = Licenciatura.history.select_related('plantel')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        #Paginate historical
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page(paginator.num_pages)
            
        #Paginate licenciaturas
        paginator1 = Paginator(licen,5)
        page1 = request.GET.get('planteles:licenciaturas')
        try:
            licen = paginator1.page(page1)
        except PageNotAnInteger:
            licen = paginator1.page(1)
        except EmptyPage:
            licen = paginator1.page(paginator1.num_pages)
        
        return render(request,'institucion/licenciatura_list.html',{'searched':searched,'model':model,'licen':licen,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        model = Licenciatura.objects.all()
        history_list = Licenciatura.history.select_related('plantel')
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        
        #Paginate historical
        paginator = Paginator(history_list,3)
        page = request.GET.get('pages')
        try:
            history_list = paginator.page(page)
        except PageNotAnInteger:
            history_list = paginator.page(1)
        except EmptyPage:
            history_list = paginator.page(paginator.num_pages)
            
        #Paginate licenciaturas
        paginator1 = Paginator(model,5)
        page1 = request.GET.get('planteles:licenciaturas')
        try:
            model = paginator1.page(page1)
        except PageNotAnInteger:
            model = paginator1.page(1)
        except EmptyPage:
            model = paginator1.page(paginator1.num_pages)
        
        return render(request,'institucion/licenciatura_list.html',{'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
        
class LicenciaturaDetailView(DetailView):
    model = Licenciatura

class LicenciaturaCreate(CreateView):
    model = Licenciatura
    form_class = LicenciaturaForms
    success_url = reverse_lazy('planteles:licenciaturas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Licenciatura.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
class LicenciaturaUpdate(UpdateView):
    model = Licenciatura
    form_class = LicenciaturaForms
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Licenciatura.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('planteles:licenciupdate',args=[self.object.id]) + '?ok'

class LicenciaturaDelete(DeleteView):
    model = Licenciatura
    success_url = reverse_lazy('planteles:licenciaturas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Licenciatura.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
# END OF LICENCIATURA

# START OF AULA
class AulaListView(ListView):
    model = Aula
    paginate_by = 8

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Aula.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        return context
    
def aulaList(request):
    if request.method == "POST":
        searched = request.POST['searched']
        aul = Aula.objects.filter(Q(clave__icontains=searched) | Q(plantel__plantel__icontains=searched))
        history_list = Aula.history.select_related('plantel')
        model = Aula.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'institucion/aula_list.html',{'searched':searched,'aul':aul,'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        history_list = Aula.history.select_related('plantel')
        model = Aula.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        return render(request,'institucion/aula_list.html',{'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    
# class AulaDetailView(DetailView):
#     model = Aula

class AulaCreate(CreateView):
    model = Aula
    form_class = AulaForms
    success_url = reverse_lazy('planteles:aulas')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Aula.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context
    
class AulaUpdate(UpdateView):
    model = Aula
    form_class = AulaForms
    template_name_suffix = '_update_form'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Aula.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('planteles:aulaupdate',args=[self.object.id]) + '?ok'
    
class AulaDelete(DeleteView):
    model = Aula
    success_url = reverse_lazy('planteles:aulas')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Aula.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

# START OF semestre o clase por semestre

def semestreList(request):
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        seme = Semestre.objects.filter(Q(semestre__icontains=searched) | Q(licenciatura__licenciatura__icontains=searched) | Q(ciclo__icontains=searched))
        print(seme.query)
        history_list = Semestre.history.select_related('licenciatura')
        model = Semestre.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        return render(request,'institucion/semestre_list.html',{'searched':searched,'seme':seme,'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
    else:
        history_list = Semestre.history.select_related('licenciatura')
        model = Semestre.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        return render(request,'institucion/semestre_list.html',{'model':model,'history_list':history_list,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente})
        
def semestreCreate(request):
    section = SemestreForms()
    sections = Semestre.objects.all()
    context = {'section':section,'sections':sections}
    if request.method == 'POST':
        section = SemestreForms(request.POST)
        if section.is_valid():
            messages.success(request,'Clase creada con exito')
            section.save()
            return redirect('/semestre-class') 
        else:
            messages.error(request,'Favor de ingresar datos correctos')
    return render(request,'institucion/semestre_form.html',context)
        
class SemestreCreate(CreateView):
    model = Semestre
    form_class = SemestreForms
    success_url = reverse_lazy('planteles:semestres')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Semestre.history.select_related('licenciatura')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        context['licenciatura'] = Licenciatura.objects.all()
        return context

class SemestreUpdate(UpdateView):
    model = Semestre
    form_class = SemestreForms
    template_name_suffix = '_update_form'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Semestre.history.select_related('licenciatura')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('planteles:semeupdate',args=[self.object.id]) + '?ok'

class SemestreDelete(DeleteView):
    model = Semestre
    success_url = reverse_lazy('planteles:semestres')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Semestre.history.select_related('licenciatura')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()
        return context

#generar tabla del horario
def TimeTableView(request,id):
    try:
        section = Semestre.objects.get(id=id)
        docema = DocenteMateria.objects.select_related('materia','docente','clase').filter(clase_id=section.id).order_by('dia','start_time')
        print(docema.query)
        time = [0] * (section.end_time - section.start_time)
        time_slot = [''] * (section.end_time - section.start_time)
        for x in range(0, len(time)):
            time_slot[x] = str(section.start_time + x) + ':00 - ' + str(section.start_time + x + 1) + ':00'
            time[x] = section.start_time + x
        context_1 = {'section':section,'docema':docema,'time':time,'time_slot':time_slot}
        return render(request,'institucion/horarioTable.html',context_1)
    except Semestre.DoesNotExist:
        messages.error(request, 'La actividad no existe')
    
        sections = Semestre.objects.all()
        context_2 = {'sections':sections}
        return render(request,'institucion/semestre_list.html',context_2)

#Generate PDF 
def horario_render_pdf_view(request,*args, **kwargs):
    pk = kwargs.get('pk')   
    horario = get_object_or_404(Semestre,pk=pk)
    docema = DocenteMateria.objects.select_related('materia','docente','clase').filter(clase_id=horario.id).order_by('dia','start_time')
    time = [0] * (horario.end_time - horario.start_time)
    time_slot = [''] * (horario.end_time - horario.start_time)
    for x in range(0, len(time)):
        time_slot[x] = str(horario.start_time + x) + ':00 - ' + str(horario.start_time + x + 1) + ':00'
        time[x] = horario.start_time + x
    
    template_path = 'institucion/pdf1.html'
    context = {'horario':horario,'docema':docema,'time':time,'time_slot':time_slot}
    #create a django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Horario.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Hay algunos errores <pre>' +html+ '</pre>')
    return response

