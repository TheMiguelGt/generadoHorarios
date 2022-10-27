from django.urls import path 
from .views import PlantelListView,PlantelCreate,PlantelDelete,LicenciaturaListView,LicenciaturaCreate,AulaListView,AulaCreate,SemestreListView,SemestreCreate

planteles_patterns = ([
    #planteles
    path('plantel/',PlantelListView.as_view(),name="planteles"),
    path('plantel/create/',PlantelCreate.as_view(),name='create'),#path de crear
    #licenciatura
    path('licenciatura/',LicenciaturaListView.as_view(),name="licenciaturas"),
    path('licenciatura/create/',LicenciaturaCreate.as_view(),name='create1'),#path de crear
    #aula
    path('aula/',AulaListView.as_view(),name="aulas"),
    path('aula/create/',AulaCreate.as_view(),name='create2'),#path de crear
    #semestre
    path('semestre/',SemestreListView.as_view(),name="semestres"),
    path('semestre/create/',SemestreCreate.as_view(),name='create3'),#path de crea
],'planteles')
