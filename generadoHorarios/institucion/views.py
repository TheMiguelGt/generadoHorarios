from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from institucion.models import Plantel,Licenciatura
from .forms import PlantelForms

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
    model = Plantel
    
class LicenciaturaDetailView(DetailView):
    model = Plantel

class LicenciaturaCreate(CreateView):
    model = Plantel
    form_class = PlantelForms
    succes_url = reverse_lazy('planteles:planteles')
    
class LicenciaturaDelete(DeleteView):
    model = Plantel
    success_url = reverse_lazy('planteles:planteles')
# END OF LICENCIATURA


    


