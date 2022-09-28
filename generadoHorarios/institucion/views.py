from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from institucion.models import Aula

# Create your views here.
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)

class AulaListView(ListView):
    model = Aula
    paginate_by = 3 