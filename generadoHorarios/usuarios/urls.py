from django.urls import path 
from usuarios import views
from .views import CoordinaListView,CoordinaDelete,AdminListView

app_name = 'usuarios'

urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('admin_signup/',views.AdminSignUp,name="AdminSignUp"),
    path('admin_list/',AdminListView.as_view(),name='administradores'),
    path('coordina_signup/',views.CoordinaSignUp,name="CoordinaSignUp"),
    path('coordina_list/',CoordinaListView.as_view(),name='coordinadores'),
    path('delete/<int:pk>',CoordinaDelete.as_view(),name='deletecoordi'),
]
