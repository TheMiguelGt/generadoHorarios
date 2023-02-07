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
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_docente or request.user.is_coordina:
            return redirect('homeUser')
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)

class StaffCoordinaRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_docente:
            return redirect("homeUser")
        return super(StaffCoordinaRequiredMixin,self).dispatch(request, *args, **kwargs)
    
# START OF PLANTELES    
@login_required(login_url="usuarios:login")
def plantelList(request):

    if request.user.is_docente or request.user.is_coordina:
        return redirect('homeUser')

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
        
class PlantelDetailView(LoginRequiredMixin,StaffRequiredMixin, DetailView):
    model = Plantel
    redirect_field_name = "usuarios:login"
    
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

class PlantelCreate(LoginRequiredMixin,StaffRequiredMixin,CreateView):
    model = Plantel
    form_class = PlantelForms
    success_url = reverse_lazy('planteles:licenciaturas')
    success_message = "Plantel creado con exito"
    redirect_field_name = "usuarios:login"
    
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

class PlantelUpdate(LoginRequiredMixin,StaffRequiredMixin,UpdateView):
    model = Plantel
    form_class = PlantelForms
    template_name_suffix = '_update_form'
    success_message = "Plantel editado con exito"
    redirect_field_name = "usuarios:login"
    
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
    
class PlantelDelete(LoginRequiredMixin,StaffRequiredMixin,DeleteView):
    model = Plantel
    success_url = reverse_lazy('planteles:planteles')
    success_message = "Plantel eliminado con exito"
    redirect_field_name = "usuarios:login"
    
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
@login_required(login_url="usuarios:login")
def licenciaturaList(request):

    if request.user.is_docente or request.user.is_coordina:
        return redirect("homeUser")

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
        plantel = Plantel.objects.all()
        if not plantel:
            messages.warning(request,'No hay planteles creados, favor de crear uno')
            return redirect('planteles:planteles')
        else:
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
        plantel = Plantel.objects.all()
        if not plantel:
            messages.warning(request,'No hay planteles creados, favor de crear uno')
            return redirect('planteles:planteles')
        else:
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
        
class LicenciaturaDetailView(LoginRequiredMixin,StaffRequiredMixin,DetailView):
    model = Licenciatura
    redirect_field_name = "usuarios:login"

class LicenciaturaCreate(LoginRequiredMixin,StaffRequiredMixin,CreateView):
    model = Licenciatura
    form_class = LicenciaturaForms
    success_url = reverse_lazy('planteles:licenciaturas')
    success_message = "Licenciatura creada con exito"
    redirect_field_name = "usuarios:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plantel'] = Plantel.objects.all()
        context['history_list'] = Licenciatura.history.select_related('plantel')
        context['pages'] = Page.objects.all()
        context['disponi'] = Disponibilidad.objects.all()
        context['matedo'] = DocenteMateria.objects.all()
        context['admin'] = Admin.objects.all()
        context['coordina'] = Coordina.objects.all()
        context['docente'] = Docente.objects.all()

        return context
    
class LicenciaturaUpdate(LoginRequiredMixin,StaffRequiredMixin,UpdateView):
    model = Licenciatura
    form_class = LicenciaturaForms
    template_name_suffix = '_update_form'
    success_message = "Licenciatura editada con exito"
    redirect_field_name = "usuarios:login"

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
        return reverse_lazy('planteles:licenciaturas')

class LicenciaturaDelete(LoginRequiredMixin,StaffRequiredMixin,DeleteView):
    model = Licenciatura
    success_url = reverse_lazy('planteles:licenciaturas')
    success_message = "Licenciatura eliminada con exito"
    redirect_field_name = "usuarios:login"

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

# START OF semestre o clase por semestre
@login_required(login_url="usuarios:login")
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
    
@login_required(login_url="usuarios:login")
def semestreCreate(request):

    if request.user.is_docente:
        return redirect("homeUser")

    licen = Licenciatura.objects.all()
    section = SemestreForms()
    sections = Semestre.objects.all()
    admin = Admin.objects.all()
    coordina = Coordina.objects.all()
    docente = Docente.objects.all()
    model = Semestre.objects.all()
    pages = Page.objects.all()
    disponi = Disponibilidad.objects.all()
    matedo = DocenteMateria.objects.all()
    context = {'section':section,'sections':sections,'pages':pages,'disponi':disponi,'matedo':matedo,'admin':admin,'coordina':coordina,'docente':docente,'licen':licen}

    if not licen: 
        messages.warning(request, 'Favor de crear una licenciatura antes de crear un horario')
        return redirect('planteles:licenciaturas')
       

    if request.method == 'POST':
        section = SemestreForms(request.POST)
        if section.is_valid():
            messages.success(request,'Horario creado con exito')
            section.save()
            return  render(request,'pages/docentemateria_list.html',context)
        else:
            messages.error(request,'Favor de ingresar datos correctos')
            
    return render(request,'institucion/semestre_form.html',context)
        
class SemestreCreate(LoginRequiredMixin,CreateView):
    model = Semestre
    form_class = SemestreForms
    success_url = reverse_lazy('planteles:semestres')
    redirect_field_name = "usuarios:login"

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

class SemestreUpdate(LoginRequiredMixin,StaffCoordinaRequiredMixin,UpdateView):
    model = Semestre
    form_class = SemestreForms
    template_name_suffix = '_update_form'
    success_message = "Horario editado con exito"
    redirect_field_name = "usuarios:login"

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
        return reverse_lazy('homeUser')

class SemestreDelete(LoginRequiredMixin,StaffCoordinaRequiredMixin,DeleteView):
    model = Semestre
    success_url = reverse_lazy('homeUser')
    success_message = "Horario eliminado con exito"
    redirect_field_name = "usuarios:login"

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
@login_required(login_url="usuarios:login")
def TimeTableView(request,id):
    try:
        section = Semestre.objects.get(id=id)
        docema = DocenteMateria.objects.select_related('materia','docente','clase').filter(clase_id=section.id).order_by('dia')
        for day in docema:
            if day.dia == 'Lunes':
                print("coco")
                day.dia == 2
                print(day.dia)
            elif day.dia == 'Miercoles':
                print("no bobo")
        results = DocenteMateria.objects.raw('SELECT * from pages_docenteMateria GROUP BY dia')
        admin = Admin.objects.all()
        coordina = Coordina.objects.all()
        docente = Docente.objects.all()
        pages = Page.objects.all()
        disponi = Disponibilidad.objects.all()
        matedo = DocenteMateria.objects.all()
        print(docema.query)
        print(results.query)
        time = [0] * (section.end_time - section.start_time)
        time_slot = [''] * (section.end_time - section.start_time)
        for x in range(0, len(time)):
            time_slot[x] = str(section.start_time + x) + ':00 - ' + str(section.start_time + x + 1) + ':00'
            time[x] = section.start_time + x
        context_1 = {'section':section,'docema':docema,'results':results,'time':time,'time_slot':time_slot,'admin':admin,'coordina':coordina,'docente':docente,'pages':pages,'disponi':disponi,'matedo':matedo}
        return render(request,'institucion/horarioTable.html',context_1)
    except Semestre.DoesNotExist:
        messages.error(request, 'La actividad no existe')
    
        sections = Semestre.objects.all()
        context_2 = {'sections':sections}
        return render(request,'institucion/semestre_list.html',context_2)

#Generate PDF 
@login_required(login_url="usuarios:login")
def horario_render_pdf_view(request,*args, **kwargs):
    pk = kwargs.get('pk')   
    horario = get_object_or_404(Semestre,pk=pk)
    docema = DocenteMateria.objects.select_related('materia','docente','clase').filter(clase_id=horario.id)
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

