from django import forms

#creo formulario de busqueda
class BusquedaConsul(forms.Form):
    #Especificar los campos
    calle = forms.CharField()
    altura = forms.IntegerField()
    localidad = forms.CharField()

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
    
