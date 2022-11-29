from django.urls import path 
from usuarios import views
from .views import CoordinaListView,CoordinaDelete,AdminListView,AdminSignUp,AdminDetailView,AdminUpdateView,DocenteListView,AlumnoListView

app_name = 'usuarios'

urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    #admin
    # path('admin_import/',views.importExcel,name="push_admin"),
    # path('admin_list/',AdminListView.as_view(),name='administradores'),
    path('admin_signup/',views.AdminSignUp,name="AdminSignUp"),
    path('admin_list/',views.adminList,name='administradores'),
    path('admin/<int:pk>/',views.AdminDetailView.as_view(),name="admin_detail"),
    path('admin/update/<int:pk>/',views.AdminUpdateView,name="admin_update"),
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
    #alumno
    path('alumno_signup/',views.AlumnoSignUp,name="AlumnoSignUp"),
    path('alumno_list/',AlumnoListView.as_view(),name='alumnos'),
    #horario
    path('horario_esc/',views.horarioEsc,name="horario"),
    #export_csv
    path('export_csv/',views.export_csv,name="export-csv"),    
]
