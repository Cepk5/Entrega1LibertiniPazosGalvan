from django import forms

#creo los formularios de busqueda

class BusquedaConsul(forms.Form):
    #Especificar los campos
    calle = forms.CharField()
    altura = forms.IntegerField()
    localidad = forms.CharField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
