from django.urls import path 
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
     path('coordina_signup/',views.CoordinaSignUp,name="CoordinaSignUp"),
]
