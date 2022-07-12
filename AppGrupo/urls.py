from django.urls import path
from AppGrupo import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('entregables', views.entregables, name="Entregables"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesores', views.profesores, name="Profesores"),
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