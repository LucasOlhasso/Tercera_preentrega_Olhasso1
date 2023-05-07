from django import forms
 
class CursoFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    curso = forms.IntegerField()