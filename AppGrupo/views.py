from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppGrupo.models import Consultorio, Especialidad, Paciente, Profesional


#importar los forms de carga y busqueda #from AppGrupo.forms import  

#Create functions

def inicio(request):
    return render(request, "AppGrupo/inicio.html")

def consultorio(request):
    return render(request, "AppGrupo/consultorio.html")

def especialidad(request):
    return render(request, "AppGrupo/especialidad.html")

def paciente(request):
    return render(request, "AppGrupo/paciente.html")

def profesional(request):
    return render(request, "AppGrupo/profesional.html")