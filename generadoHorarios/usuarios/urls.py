from django.urls import path 
from usuarios import views
from django.contrib.auth.decorators import login_required
from .views import ProfileView,CoordinaUpView,CoordinaDelete,AdminSignUp,AdminDetailView,AdminUpView,DocenteListView,DocenteUpView,AlumnoListView,ControlUsers

app_name = 'usuarios'

urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    #control_users
    path('control_users/',ControlUsers.as_view(),name="control_users"),
    #admin
    path('admin_signup/',views.AdminSignUp,name="AdminSignUp"),
    path('admin_list/',views.adminList,name='administradores'),
    path('admin/<int:pk>/',views.AdminDetailView.as_view(),name="admin_detail"),
    #coordina
    # path('coordina_list/',CoordinaListView.as_view(),name='coordinadores'),
    path('coordina_signup/',views.CoordinaSignUp,name="CoordinaSignUp"),
    path('coordina_import/',views.coordina_upload,name='coordina_load'),
    path('coordina_list/',views.coordinaList,name='coordinadores'),
    path('delete/<int:pk>',CoordinaDelete.as_view(),name='deletecoordi'),
    #docente
    # path('docente_list/',DocenteListView.as_view(),name='docentes'),
    path('docente_signup/',views.DocenteSignUp,name="DocenteSignUp"),
    path('docente_import/',views.docente_upload,name='docente_load'),
    path('docente_list/',views.docenteList,name='docentes'),
    #update profile
    path('admin_update/',AdminUpView.as_view(),name="admin_update"),
    path('coordina_update/',CoordinaUpView.as_view(),name="coordina_profile"),
    path('docente_update/',DocenteUpView.as_view(),name="docente_update"),
    #profile view
    path('profile/',ProfileView.as_view(),name="profile_view"),
    #alumno
    path('alumno_signup/',views.AlumnoSignUp,name="AlumnoSignUp"),
    path('alumno_list/',AlumnoListView.as_view(),name='alumnos'),
    #horario
    path('horario_esc/',views.horarioEsc,name="horario"),
    #export_csv
    path('export_csv/',views.export_csv,name="export-csv"),    
]
