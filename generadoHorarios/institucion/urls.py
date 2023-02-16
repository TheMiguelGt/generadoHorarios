from django.urls import path 
from institucion import views
from .views import PlantelCreate,PlantelUpdate,PlantelDelete,LicenciaturaCreate,LicenciaturaUpdate,LicenciaturaDelete,horario_render_pdf_view

planteles_patterns = ([
    #planteles
    path('plantel/',views.plantelList,name='planteles'),
    path('plantel/create/',PlantelCreate.as_view(),name='create'),#path de crear
    path('plantel/update/<int:pk>/',PlantelUpdate.as_view(),name="planupdate"),
    path('plantel/delete/<int:pk>/',PlantelDelete.as_view(),name="plandel"),
    #licenciatura
    path('licenciatura/',views.licenciaturaList,name='licenciaturas'),
    path('licenciatura/create/',LicenciaturaCreate.as_view(),name='create1'),#path de crear
    path('licenciatura/update/<int:pk>/',LicenciaturaUpdate.as_view(),name="licenupdate"),
    path('licenciatura/delete/<int:pk>/',LicenciaturaDelete.as_view(),name="licendele"),
    #semestre
    # path('semestre-class/create/',views.semestreCreate,name='create3'),
    # path('semestre-class/update/<int:pk>/',SemestreUpdate.as_view(),name="semeupdate"),
    # path('semestre-class/delete/<int:pk>/',SemestreDelete.as_view(),name="semedel"),
    #tabla del horario
    path('semestre-class/horario/<str:id>/',views.TimeTableView,name='timetable'),
    path('semestre-class/horario/pdf/<pk>/',horario_render_pdf_view,name='horario-pdf-view'),
],'planteles')
