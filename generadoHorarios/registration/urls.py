from urllib.parse import urlparse
from django.urls import path 
# from .views import SignUpView,ProfileUpdate,AlumDetailView
from .views import AlumDetailView,DoceDetailView
from . import views

urlpatterns = [
    # path('signup/',SignUpView.as_view(),name="signup"),
    # #path('profile/',ProfileUpdate.as_view(),name="profile"),
    # #alumno
    path('alumno/<int:pk>/',AlumDetailView.as_view(),name="alumno_detail"),
    path('docente/<int:pk>/',DoceDetailView.as_view(),name="docente_detail"),
    #registrar usuarios
    path('import_docente/',views.importDocentes,name="importDoce"),
]

