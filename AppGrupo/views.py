from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppGrupo.models import Cursos, Estudiantes, Profesores, Entregables


#importar los forms de carga y busqueda #from AppGrupo.forms import  

#Create functions

def inicio(request):
    return render(request, "AppGrupo/inicio.html")

def cursos(request):
    return render(request, "AppGrupo/cursos.html")

def entregables(request):
    return render(request, "AppGrupo/entregables.html")

def estudiantes(request):
    return render(request, "AppGrupo/estudiantes.html")

def profesores(request):
    return render(request, "AppGrupo/profesores.html")