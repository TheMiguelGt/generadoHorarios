from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from institucion.models import Aula, Plantel,Licenciatura
from .forms import PlantelForms,LicenciaturaForms,AulaForms

# Create your views here.
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)

# START OF PLANTELES
class PlantelListView(ListView):
    model = Plantel
    
class PlantelDetailView(DetailView):
    model = Plantel

class PlantelCreate(CreateView):
    model = Plantel
    form_class = PlantelForms
    success_url = reverse_lazy('planteles:planteles')
    
class PlantelDelete(DeleteView):
    model = Plantel
    success_url = reverse_lazy('planteles:planteles')
# END OF PLANTELES

# START OF LICENCIATURA
class LicenciaturaListView(ListView):
    model = Licenciatura
    
class LicenciaturaDetailView(DetailView):
    model = Licenciatura

class LicenciaturaCreate(CreateView):
    model = Licenciatura
    form_class = LicenciaturaForms
    succes_url = reverse_lazy('planteles:licenciaturas')
    
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
    succes_url = reverse_lazy('planteles:aulas')
    
# class AulaDelete(DeleteView):
#     model = Aula
#     success_url = reverse_lazy('planteles:aulas')
# END OF AULA


    


