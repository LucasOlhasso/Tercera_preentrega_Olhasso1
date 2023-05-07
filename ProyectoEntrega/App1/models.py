from django.db import models

# Estos son los modelos.
class Pacientes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()

class Profesional(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Turno(models.Model):
    nombrepaciente= models.CharField(max_length=50) #por ahora no están vinculados entre tablas
    nombreprofesional= models.CharField(max_length=50) #por ahora no están vinculados entre tablas
    fechaturno= models.DateField()
    turnovigente= models.BooleanField()
    