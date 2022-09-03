from django.urls import path
from .views import LoginPageView,SignupPageView

urlpatterns = [
    #usuario paths 
    path('login/',LoginPageView.as_view(),name="login"),#vista del login
    path('signup/',SignupPageView.as_view(),name="signup"), #vista del signup
]
