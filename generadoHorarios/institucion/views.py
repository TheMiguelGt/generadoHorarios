from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from institucion.models import Aula, Plantel,Licenciatura, Semestre
from .forms import PlantelForms,LicenciaturaForms,AulaForms,SemestreForms

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
        return context
    
class PlantelDetailView(DetailView):
    model = Plantel

class PlantelCreate(CreateView):
    model = Plantel
    form_class = PlantelForms
    success_url = reverse_lazy('planteles:planteles')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        return context

class PlantelUpdate(UpdateView):
    model = Plantel
    form_class = PlantelForms
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        return context
    
    def get_success_url(self):
        return reverse_lazy('pages:planupdate',args=[self.object.id]) + '?ok'
    
class PlantelDelete(DeleteView):
    model = Plantel
    success_url = reverse_lazy('planteles:planteles')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_list'] = Plantel.history.all()
        return context
# END OF PLANTELES

# START OF LICENCIATURA
class LicenciaturaListView(ListView):
    model = Licenciatura
    
class LicenciaturaDetailView(DetailView):
    model = Licenciatura

class LicenciaturaCreate(CreateView):
    model = Licenciatura
    form_class = LicenciaturaForms
    success_url = reverse_lazy('planteles:licenciaturas')
    
    
class LicenciaturaDelete(DeleteView):
    model = Licenciatura
    success_url = reverse_lazy('planteles:licenciaturas')
# END OF LICENCIATURA

# START OF AULA
class AulaListView(ListView):
    model = Aula
    
# class AulaDetailView(DetailView):
#     model = Aula

class AulaCreate(CreateView):
    model = Aula
    form_class = AulaForms
    success_url = reverse_lazy('planteles:aulas')
    
# class AulaDelete(DeleteView):
#     model = Aula
#     success_url = reverse_lazy('planteles:aulas')
# END OF AULA

# START OF AULA
class SemestreListView(ListView):
    model = Semestre
    
# class AulaDetailView(DetailView):
#     model = Aula

class SemestreCreate(CreateView):
    model = Semestre
    form_class = SemestreForms
    success_url = reverse_lazy('planteles:semestres')
    
# class AulaDelete(DeleteView):
#     model = Aula
#     success_url = reverse_lazy('planteles:aulas')
# END OF AULA

    


