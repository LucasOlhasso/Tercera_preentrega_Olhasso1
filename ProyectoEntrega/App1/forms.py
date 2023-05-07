from django import forms
 
class PacientesFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()

class ProfesionalFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class TurnosFormulario(forms.Form):
    id= forms.IntegerField()
    nombrepaciente= forms.CharField(max_length=30)
    nombreprofesional= forms.CharField(max_length=30)
    fechaturno= forms.DateField()
    turnovigente= forms.BooleanField()  