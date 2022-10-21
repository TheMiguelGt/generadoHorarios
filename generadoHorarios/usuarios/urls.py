from django.urls import path 
from usuarios import views
from .views import CoordinaListView,CoordinaDelete

app_name = 'usuarios'

urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('coordina_signup/',views.CoordinaSignUp,name="CoordinaSignUp"),
    path('',CoordinaListView.as_view(),name='coordinadores'),
    path('delete/<int:pk>',CoordinaDelete.as_view(),name='deletecoordi'),
]
