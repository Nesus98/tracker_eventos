from django.contrib import admin
from django.urls import path, include # <-- Súper importante importar 'include'
from eventos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_eventos, name='lista_eventos'),
    
    # Esta línea activa automáticamente rutas como /accounts/login/ y /accounts/logout/
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Tus rutas de añadir
    path('añadir_evento/', views.crear_evento, name='crear_evento'),
    path('añadir_candidatura/', views.crear_candidatura, name='crear_candidatura'),
    
    # Tus rutas de editar y eliminar
    path('eventos/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('candidaturas/<int:pk>/editar/', views.editar_candidatura, name='editar_candidatura'),
    path('eliminar/<int:candidatura_id>/', views.eliminar_candidatura, name='eliminar_candidatura'),
]