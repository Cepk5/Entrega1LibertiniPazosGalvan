from django.db import models

#create models

class Consultorio(models.Model):
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    localidad = models.CharField(max_length=30)

class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    titulo = models.CharField(max_length=40)

class Especialidad(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()





