from django.urls import path 
from institucion import views
from .views import PlantelListView,PlantelCreate,PlantelUpdate,PlantelDelete,LicenciaturaListView,LicenciaturaCreate,LicenciaturaUpdate,LicenciaturaDelete,AulaListView,AulaCreate,AulaUpdate,AulaDelete,SemestreListView,SemestreCreate,SemestreUpdate,SemestreDelete,CicloCreate,CicloDelete,CicloUpdate

planteles_patterns = ([
    #planteles
    # path('plantel/',PlantelListView.as_view(),name="planteles"),
    path('plantel/',views.plantelList,name='planteles'),
    path('plantel/create/',PlantelCreate.as_view(),name='create'),#path de crear
    path('plantel/update/<int:pk>/',PlantelUpdate.as_view(),name="planupdate"),
    path('plantel/delete/<int:pk>/',PlantelDelete.as_view(),name="plandel"),
    #licenciatura
    # path('licenciatura/',LicenciaturaListView.as_view(),name="licenciaturas"),
    path('licenciatura/',views.licenciaturaList,name='licenciaturas'),
    path('licenciatura/create/',LicenciaturaCreate.as_view(),name='create1'),#path de crear
    path('licenciatura/update/<int:pk>/',LicenciaturaUpdate.as_view(),name="licenupdate"),
    path('licenciatura/delete/<int:pk>/',LicenciaturaDelete.as_view(),name="licendele"),
    #aula
    # path('aula/',AulaListView.as_view(),name="aulas"),
    path('aula/',views.aulaList,name='aulas'),
    path('aula/create/',AulaCreate.as_view(),name='create2'),#path de crear
    path('aula/update/<int:pk>/',AulaUpdate.as_view(),name="aulaupdate"),
    path('aula/delete/<int:pk>/',AulaDelete.as_view(),name="auladel"),
    #semestre
    # path('semestre/',SemestreListView.as_view(),name="semestres"),
    path('semestre/',views.semestreList,name='semestres'),
    path('semestre/create/',SemestreCreate.as_view(),name='create3'),#path de crea
    path('semestre/update/<int:pk>/',SemestreUpdate.as_view(),name="semeupdate"),
    path('semestre/delete/<int:pk>/',SemestreDelete.as_view(),name="semedel"),
    #ciclo
    path('ciclo/',views.cicloList,name='ciclos'),
    path('ciclo/create/',CicloCreate.as_view(),name='createcic'),#path de crea
    path('ciclo/update/<int:pk>/',CicloUpdate.as_view(),name="cicupdate"),
    path('ciclo/delete/<int:pk>/',CicloDelete.as_view(),name="cicdel"),
],'planteles')
