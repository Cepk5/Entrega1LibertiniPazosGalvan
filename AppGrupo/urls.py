from django.urls import path
from .views import *

urlpatterns = [
   
    path('', inicio, name="Inicio"),
    path('consultorio', consultorio, name="Consultorio"),
    path('especialidad', especialidad, name="Especialidad"),
    path('paciente', paciente, name="Paciente"),
    path('profesional', profesional, name="Profesional"),
    path('consultorioForm', consultorioForm, name='ConsultorioForm'),
]
