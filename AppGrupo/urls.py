from django.urls import path
from AppGrupo import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('consultorio', views.consultorio, name="Consultorio"),
    path('especialidad', views.especialidad, name="Especialidad"),
    path('paciente', views.paciente, name="Paciente"),
    path('profesional', views.profesional, name="Profesional"),
    path('busquedaconsultorio', views.busquedaConsul, name="BusquedaConsul"),
    path('buscar', views.buscar),
]