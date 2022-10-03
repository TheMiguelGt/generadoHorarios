# from .forms import UserCreationFormWithEmail, ProfileForm
from django.shortcuts import  render 
from django.views.generic import CreateView,DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from tablib import Dataset #importar excel
from django.urls import reverse_lazy
from django import forms
# from .models import Profile,Alumno
from .models import Alumno,Docente
from .resource import DocenteResource

# Create your views here.
# class SignUpView(CreateView):
#     form_class = UserCreationFormWithEmail
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'
    
#     def get_success_url(self):#si fue con exito se le agrega algo al url
#         return reverse_lazy('login')+'?register'

#     def get_form(self,form_class=None):
#         form = super(SignUpView,self).get_form()
#         #modificar en tiempo real
#         form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
#         form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Correo'})
#         form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Password'})
#         form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Confirmar password'})
        
#         return form

# @method_decorator(login_required,name='dispatch')
# class ProfileUpdate(UpdateView):
#     form_class = ProfileForm
#     success_url = reverse_lazy('profile')
#     template_name = 'registration/profile_form.html'

#     def get_object(self):
#         #recuperar el objeto que se editara
#         profile, created = Profile.objects.get_or_create(user=self.request.user)#consigue o crea mediante el filtro
#         return profile
    
#logout view
@method_decorator(login_required,name='dispatch')
class AlumDetailView(DetailView):
    context_object_name = "alumno"
    model = Alumno
    template_name = 'registration/alumno_detail.html'

@method_decorator(login_required,name='dispatch')
class DoceDetailView(DetailView):
    context_object_name = "alumno"
    model = Docente
    template_name = 'registration/docente_detail.html'
    
@method_decorator(login_required,name='dispatch')
def importDocentes(request):
    #template_name = 'registration/alta_docente.html'
    docente_resource = DocenteResource()
    dataset = Dataset()
    print(dataset)
    nuevos_docentes = request.FILES['xlsfile']
    print(nuevos_docentes)
    imported_data = dataset.load(nuevos_docentes.read())
    print(dataset)
    result = docente_resource.import_data(dataset, dry_run=True)
    #test the data import 
    print(result.has_errors())
    if not result.has_errors():
        docente_resource.import_data(dataset,dry_run=False)# Actually import now  return render(request, 'export/importar.html')  
    return render(request, 'registration/importDocentes.html')
    
