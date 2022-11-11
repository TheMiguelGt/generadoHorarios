from django.urls import path,include
from core import views 
from .views import HomePageView,UserPageView

urlpatterns = [
     #core paths
     path('',HomePageView.as_view(),name="home"),#vista del home
     path('home/',views.homePage2View,name="homeUser"),
     path('admn/',UserPageView.as_view(),name="userPage"),
]
