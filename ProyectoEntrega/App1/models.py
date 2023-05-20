from django.db import models
import datetime

# Estos son los modelos.
class Pacientes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Dni: {self.dni}"

class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.mail} - Profesión: {self.profesion}"

class Turno(models.Model):
    nombrepaciente= models.CharField(max_length=50) #por ahora no están vinculados entre tablas
    nombreprofesional= models.CharField(max_length=50) #por ahora no están vinculados entre tablas
    fechaturno = models.DateField(default=datetime.date.today)
    turnovigente= models.BooleanField()


    