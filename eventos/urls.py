from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('candidaturas/<int:pk>/editar/', views.editar_candidatura, name='editar_candidatura'),
    path('candidaturas/<int:pk>/eliminar/', views.eliminar_candidatura, name='eliminar_candidatura'),
]
