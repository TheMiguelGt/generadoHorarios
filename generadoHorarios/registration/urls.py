from urllib.parse import urlparse
from django.urls import path 
from .views import SignUpView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name="signup"),
]

