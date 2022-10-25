from django.urls import path 
from .views import PlantelListView,PlantelCreate,PlantelDelete

planteles_patterns = ([
    path('',PlantelListView.as_view(),name="planteles"),
    path('create/',PlantelCreate.as_view(),name='create'),#path de crear
],'planteles')
