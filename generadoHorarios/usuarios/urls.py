from django.urls import path
from .views import LoginPageView

urlpatterns = [
    #usuario paths 
    path('',LoginPageView.as_view(),name="login"),#vista del login
]
