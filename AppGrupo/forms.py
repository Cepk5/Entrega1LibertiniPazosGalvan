from django import forms

class ConsultorioForm(forms.Form):
    calle = forms.CharField()
    altura = forms.IntegerField()
    localidad = forms.CharField()

class ProfesionalForm(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class EspecialidadForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=40)

class PacienteForm(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    