from django.urls import path
from usuarios import views
from pages import views
from .views import PageListView,PageDetailView,PageCreate,PageUpdate,PageDelete,DoceMateListView,DoceMateCreate,DispoListView,DispoCreate

pages_patterns = ([ #se crea una tupla
    #MATERIAS
    path('materia/',PageListView.as_view(), name='pages'), #se usan las clases y se declaran como vistas
    path('materia/<int:pk>/<slug:slug>/',PageDetailView.as_view(), name='page'), #se cambio el id por pk y slug_page por solo slug
    path('materia/create/',PageCreate.as_view(),name='create'),#path de crear
    path('materia/update/<int:pk>/',PageUpdate.as_view(),name="update"),#se manda la pagina actualizada o que se actualizara
    path('materia/delete/<int:pk>/',PageDelete.as_view(),name="delete"),
    #DOCENTE MATERIA
    path('docemate/',DoceMateListView.as_view(), name='docemates'),
    path('docemate/create/',DoceMateCreate.as_view(),name='createm'),
    #DISPONIBILIDAD DOCENTE
    path('disponibilidad/',DispoListView.as_view(), name='disponi'),
    path('disponibilidad/create/',DispoCreate.as_view(),name='createdi'),
    #HORARIO
    path('horario/',views.AlumnoSignUp,name="horario"),
],'pages')
