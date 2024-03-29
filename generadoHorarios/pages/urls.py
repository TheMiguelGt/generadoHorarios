from django.urls import path
from pages import views
from .views import PageDetailView,PageCreate,PageUpdate,PageDelete,DoceMateDetail,DoceMateCreate,DoceMateUpdate,DoceMateDelete

pages_patterns = ([ #se crea una tupla
    #MATERIAS
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
],'pages')
