from django.urls import path 
from .views import HomePageView,HomeUserView

urlpatterns = [
     #core paths
     path('',HomePageView.as_view(),name="home"),#vista del home
     path('home/',HomeUserView.as_view(),name="homeUser"),
]
