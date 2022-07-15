from locale import ALT_DIGITS
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppGrupo.models import Consultorio, Especialidad, Paciente, Profesional
from AppGrupo.forms import ConsultorioForm, EspecialidadForm, PacienteForm, ProfesionalForm


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

def consultorioForm(request):
    if request.method == 'POST':
        miFormulario = ConsultorioForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            calle=info['calle']
            altura=info['altura']
            localidad=info['localidad']
            consultorio=Consultorio(calle=calle, altura=altura, localidad=localidad)
            consultorio.save()
            return render(request, 'AppGrupo/inicio.html')
    else:
        miFormulario = ConsultorioForm()
    return render(request, 'AppGrupo/consultorioForm.html', {'miFormulario': miFormulario})

def especialidadForm(request):
    if request.method == 'POST':
        miFormulario = EspecialidadForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            nombre=info['nombre']
            tipo=info['tipo']
            especialidad=Especialidad(nombre=nombre, tipo=tipo)
            especialidad.save()
            return render(request, 'AppGrupo/inicio.html')
    else:
        miFormulario = EspecialidadForm()
    return render(request, 'AppGrupo/especialidadForm.html', {'miFormulario': miFormulario})

def pacienteForm(request):
    if request.method == 'POST':
        miFormulario = PacienteForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            email=info['email']
            paciente=Paciente(nombre=nombre, apellido=apellido, email=email)
            paciente.save()
            return render(request, 'AppGrupo/inicio.html')
    else:
        miFormulario = EspecialidadForm()
    return render(request, 'AppGrupo/pacienteForm.html', {'miFormulario': miFormulario})

def profesionalForm(request):
    if request.method == 'POST':
        miFormulario = ProfesionalForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            titulo=info['titulo']
            profesional=Profesional(nombre=nombre, apellido=apellido, titulo=titulo)
            profesional.save()
            return render(request, 'AppGrupo/inicio.html')
    else:
        miFormulario = ProfesionalForm()
    return render(request, 'AppGrupo/profesionalForm.html', {'miFormulario': miFormulario})