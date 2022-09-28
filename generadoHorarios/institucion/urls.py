from django.urls import path 
from .views import AulaListView

aulas_patterns = ([
    path('',AulaListView.as_view(),name="aulas"),
],'aulas')
