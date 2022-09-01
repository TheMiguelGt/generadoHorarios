from django.shortcuts import render
from multiprocessing import context
from django.views.generic import TemplateView

# Create your views here.
class LoginPageView(TemplateView):
    template_name = 'usuarios/login.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'title':'Login'})
    
