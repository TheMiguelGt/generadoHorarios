from django.urls import path 
from .views import PlantelListView,PlantelCreate,PlantelDelete,LicenciaturaListView,LicenciaturaCreate

planteles_patterns = ([
    #planteles
    path('plantel/',PlantelListView.as_view(),name="planteles"),
    path('plantel/create/',PlantelCreate.as_view(),name='create'),#path de crear
    #licenciatura
    path('licenciatura/',LicenciaturaListView.as_view(),name="licenciaturas"),
    path('licenciatura/create/',LicenciaturaCreate.as_view(),name='create1'),#path de crear
],'planteles')
