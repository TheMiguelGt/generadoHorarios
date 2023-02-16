from django.urls import path
from django.contrib.auth.decorators import login_required
from core import views 
from .views import HomePageView,UserPageView,SemestreUpdate,SemestreDelete,semeCreate

urlpatterns = [
     #core paths
     path('',HomePageView.as_view(),name="home"),#vista del home
     path('home/',views.homePage2View,name="homeUser"),
     #semestre
     # path('semestre-class/create/',views.semestreCreate,name='create3'),
     path('semestre-class/create/',semeCreate.as_view(),name='create3'),
     path('semestre-class/update/<int:pk>/',SemestreUpdate.as_view(),name="semeupdate"),
     path('semestre-class/delete/<int:pk>/',SemestreDelete.as_view(),name="semedel"),
     path('admn/',UserPageView.as_view(),name="userPage"),
]
