from django.urls import path 
from .views import HomePageView

urlpatterns = [
     #core paths
     path('',HomePageView.as_view(),name="home"),#vista del home
]
