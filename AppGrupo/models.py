from django.db import models

#create models

class Consultorio(models.Model):
    #nombre = models.CharField(max_length=40)
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    localidad = models.CharField(max_length=30)

    def __str__(request):
        return request.calle

class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    titulo = models.CharField(max_length=40)

    def __str__(request):
        return request.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)

    def __str__(request):
        return request.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(request):
        return request.nombre





