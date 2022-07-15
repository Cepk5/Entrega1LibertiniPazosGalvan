from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppGrupo.models import Consultorio, Especialidad, Paciente, Profesional
from AppGrupo.forms import BusquedaConsul


#importar los forms de carga y busqueda from AppGrupo.forms import  

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

#recibo el apiform

def busquedaConsul(request):
    return render(request, "AppGrupo/busquedaconsultorio.html")

def buscar(request):
    
    if request.GET["localidad"]:

        localidad = request.GET['localidad']
        consultorio = Consultorio.objects.filter(localidad__icontains=localidad)

        return render(request, "AppGrupo/buscar.html", {"localidad":localidad, "consultorio":consultorio})
    
    else:

        respuesta = "Completa el campo de busqueda"

    return render(request, "AppGrupo/buscar.html", {"respuesta":respuesta})