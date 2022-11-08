from django.urls import path 
from .views import PlantelListView,PlantelCreate,PlantelUpdate,PlantelDelete,LicenciaturaListView,LicenciaturaCreate,LicenciaturaUpdate,LicenciaturaDelete,AulaListView,AulaCreate,SemestreListView,SemestreCreate

planteles_patterns = ([
    #planteles
    path('plantel/',PlantelListView.as_view(),name="planteles"),
    path('plantel/create/',PlantelCreate.as_view(),name='create'),#path de crear
    path('plantel/update/<int:pk>/',PlantelUpdate.as_view(),name="planupdate"),
    path('plantel/delete/<int:pk>/',PlantelDelete.as_view(),name="plandel"),
    #licenciatura
    path('licenciatura/',LicenciaturaListView.as_view(),name="licenciaturas"),
    path('licenciatura/create/',LicenciaturaCreate.as_view(),name='create1'),#path de crear
    path('licenciatura/update/<int:pk>/',LicenciaturaUpdate.as_view(),name="licenupdate"),
    path('licenciatura/delete/<int:pk>/',LicenciaturaDelete.as_view(),name="licendel"),
    #aula
    path('aula/',AulaListView.as_view(),name="aulas"),
    path('aula/create/',AulaCreate.as_view(),name='create2'),#path de crear
    #semestre
    path('semestre/',SemestreListView.as_view(),name="semestres"),
    path('semestre/create/',SemestreCreate.as_view(),name='create3'),#path de crea
],'planteles')
