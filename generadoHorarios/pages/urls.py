from django.urls import path
from .views import PageListView,PageDetailView

urlpatterns = [
    path('',PageListView.as_view(), name='pages'), #se usan las clases y se declaran como vistas
    path('<int:pk>/<slug:slug>/',PageDetailView.as_view(), name='page'), #se cambio el id por pk y slug_page por solo slug
]
