from django.urls import path 
from .views import HomePageView,HomePage2View

urlpatterns = [
     #core paths
     path('',HomePageView.as_view(),name="home"),#vista del home
     path('home/',HomePage2View.as_view(),name="homeUser"),
]
