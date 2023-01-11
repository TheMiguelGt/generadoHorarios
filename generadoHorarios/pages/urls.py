from django.urls import path
from pages import views
from .views import PageListView,PageDetailView,PageCreate,PageUpdate,PageDelete,DoceMateDetail,DoceMateCreate,DoceMateUpdate,DoceMateDelete,DispoListView,DispoCreate,DispoUpdate,DispoDelete,DiaList,DiaCreate,DiaUpdate,HoraCreate,HoraUpdate

pages_patterns = ([ #se crea una tupla
    #MATERIAS
    # path('materia/',PageListView.as_view(), name='pages'), #se usan las clases y se declaran como vistas
    path('materia/',views.pageListSearch,name='pages'),
    path('materia/<int:pk>/<slug:slug>/',PageDetailView.as_view(), name='page'), #se cambio el id por pk y slug_page por solo slug
    path('materia/create/',PageCreate.as_view(),name='create'),#path de crear
    path('materia/update/<int:pk>/',PageUpdate.as_view(),name="update"),#se manda la pagina actualizada o que se actualizara
    path('materia/delete/<int:pk>/',PageDelete.as_view(),name="delete"),
    #DOCENTE MATERIA
    path('docemate/',views.DoceMateListView, name='docemates'),
    path('docemate/<int:pk>/<slug:slug>/',DoceMateDetail.as_view(),name='docemate'),
    path('docemate/create/',DoceMateCreate.as_view(),name='createm'),
    path('docemate/update/<int:pk>/',DoceMateUpdate.as_view(),name='doceupdate'),
    path('docemate/delete/<int:pk>/',DoceMateDelete.as_view(),name="docedel"),
    #DISPONIBILIDAD DOCENTE
    # path('disponibilidad/',DispoListView.as_view(), name='disponi'),
    path('disponibilidad/',views.dispoListSearch,name='disponi'),
    path('disponibilidad/create/',DispoCreate.as_view(),name='createdi'),
    path('disponibilidad/update/<int:pk>/',DispoUpdate.as_view(),name='dispoupdate'),
    path('disponibilidad/delete/<int:pk>/',DispoDelete.as_view(),name="dispodel"),
    #DIA 
    path('dia/',DiaList.as_view(),name='dias'),
    path('dia/create/',DiaCreate.as_view(),name='createdia'),
    path('dia/update/<int:pk>/',DiaUpdate.as_view(),name='diaupdate'),
    #HORA
    path('hora/',views.HoraList,name='horas'),
    path('hora/create/',HoraCreate.as_view(),name='createhora'),
    path('hora/update/<int:pk>/',HoraUpdate.as_view(),name='horaupdate'),
],'pages')
