from django.urls import path 
from .views import PlantelListView

planteles_patterns = ([
    path('',PlantelListView.as_view(),name="planteles"),
],'planteles')
