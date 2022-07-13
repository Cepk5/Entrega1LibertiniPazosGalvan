from django.urls import path
from AppGrupo import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('consultorio', views.consultorio, name="Consultorio"),
    path('especialidad', views.especialidad, name="Especialidad"),
    path('paciente', views.paciente, name="Paciente"),
    path('profesional', views.profesional, name="Profesional"),
]

"""
importo las url de los html
urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
----------------- hasta aca tendria los mismos nombres, falta usar el name
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),

]

"""