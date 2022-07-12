from django.db import models

#create models

class Cursos(models.Model):
    curso = models.CharField(max_length=30)
    comision = models.IntegerField()

class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    feEntrega = models.DateField()
    entregado = models.BooleanField()

class Estudiantes(models.Model):
    nom = models.CharField(max_length=40)
    ape = models.CharField(max_length=40)
    feNac = models.DateField()
    email = models.EmailField()

class Profesores(models.Model):
    nom = models.CharField(max_length=40)
    ape = models.CharField(max_length=40)
    email = models.EmailField()





