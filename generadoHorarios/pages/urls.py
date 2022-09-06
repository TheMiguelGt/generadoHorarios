from django.urls import path
from .views import PageListView,PageDetailView,PageCreate

pages_patterns = ([ #se crea una tupla
    path('',PageListView.as_view(), name='pages'), #se usan las clases y se declaran como vistas
    path('<int:pk>/<slug:slug>/',PageDetailView.as_view(), name='page'), #se cambio el id por pk y slug_page por solo slug
    path('create/',PageCreate.as_view(),name='create')#path de crear
],'pages')
