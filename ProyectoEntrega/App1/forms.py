from django import forms

 
class PacientesFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()

class ProfesionalFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
    profesion = forms.CharField()

class TurnosFormulario(forms.Form):
    id= forms.IntegerField()
    nombrepaciente= forms.CharField(max_length=30)
    nombreprofesional= forms.CharField(max_length=30)
    fechaturno= forms.DateField()
    turnovigente= forms.BooleanField()  
    