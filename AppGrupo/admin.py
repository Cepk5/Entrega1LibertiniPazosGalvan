from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Consultorio)
admin.site.register(Especialidad)
admin.site.register(Paciente)
admin.site.register(Profesional)